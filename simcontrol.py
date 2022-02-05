import bindings
from SimConnect import *

class Simcontrol:
    def __init__(self):
        self.sm = SimConnect()
        self.aq = AircraftRequests(self.sm)
        self.ae = AircraftEvents(self.sm)


    def quit_connect(self):
        self.sm.exit()

    def scenarios_search(name, value):
        try:
            find_scenario = next(item for item in bindings.scenarios if item["name"] == str(name))
            return find_scenario[value]
        except:
            print ("Error while searching scenarios")

    
    def input_distributor(self, key):
        try:
            key = bindings.bindings[key]
        except:
            None

        if 'MobiFlight' in key:
            try:
                self.mobiflight_event(key)
            except:
                print ("Error while executing MobiFlight event")
            pass

        if "@" in key:
            try:
                self.event(key, self.scenarios_search(key, "id"), self.scenarios_search(key, "value"), True)
            except:
                print ("Error while executing scenario")
            pass

        try:
            self.event(key)
        except:
            print ("Error while executing event")

        
    def event(self, key, ID=None, value=None, isscenario=False):
        if isscenario:
            trigger = self.ae.find(ID)
            trigger(value)
        else:
            trigger = self.ae.find(key)
            trigger()


    def request(self, key):
        return self.aq.get(key)

    
    def mobiflight_event(self, key):
        key = key.encode('utf-8')
        mbfl_trigger = Event(key, self.sm)
        mbfl_trigger()
