from SimConnect import *
from bindings import bindings


class Simcontrol:
    def __init__(self):
        self.sm = SimConnect()
        self.aq = AircraftRequests(self.sm)
        self.ae = AircraftEvents(self.sm)


    def quit_connect(self):
        self.sm.exit()
        quit()


    def event(self, key):
        key = bindings[key.decode('utf-8')]
        if 'MobiFlight' in key:
            self.mobiflight_event(key)
        if 'BARO_STD' == key:
            trigger = self.ae.find('KOHLSMAN_SET')
            trigger(1013)
        else:
            trigger = self.ae.find(key)
            trigger()


    def request(self, key):
        return self.aq.get(key)

    
    def mobiflight_event(self, key):
        key = key.encode('utf-8')
        mbfl_trigger = Event(key, self.sm)
        mbfl_trigger()
