import bindings
from SimConnect import *

class Simcontrol:
    def __init__(self):
        self.sm = SimConnect()
        self.aq = AircraftRequests(self.sm)
        self.ae = AircraftEvents(self.sm)


    def quit_connect(self):
        self.sm.exit()


    def scenarios_search(self, name, value):
        try:
            find_scenario = next(item for item in bindings.scenarios if item["name"] == str(name))
            return find_scenario[value]
        except:
            print ("Error while searching scenarios")

    
    def input_distributor(self, key):
        #Getting a binding if simple data recieved. e.g. "24B" from pyFlightBox search for binding named "24B" in bindings.py.
        try:
            key = bindings.bindings[key]
        except:
            None #If there is no binding (like potentiometers data %POT_NAME%:%value%)-> input data transmitting below.

        #If binding contains "MobiFlight" in it.
        if 'MobiFlight' in key:
            try:
                self.mobiflight_event(key)
            except:
                print ("Error while executing MobiFlight event")
            return

        #If binding contains scenario marker "@" in it.
        if "@" in key:
            try:
                self.event(self.scenarios_search(key, "id"), self.scenarios_search(key, "value"), True)
            except:
                print ("Error while executing @ scenario")
            return

        #If binding contains multidata marker ":" in it. E.g. potentiometer data THROTTLE:998 splits for "THROTTLE" binding and value 998
        if ":" in key:
            try:
                a = key.split(":")
                self.event(bindings.bindings[a[0]], int(a[1]), True)
            except:
                print ("Error while executing : scenario")
            return

        try:
            self.event(key)
        except:
            print ("Error while executing event")

        
    def event(self, ID, value=None, isscenario=False):

        if isscenario:
            trigger = self.ae.find(ID)
            trigger(value)
        else:
            trigger = self.ae.find(ID)
            trigger()


    def request(self, key):
        return self.aq.get(key)

    
    def mobiflight_event(self, ID):
        ID = ID.encode('utf-8')
        mbfl_trigger = Event(ID, self.sm)
        mbfl_trigger()
