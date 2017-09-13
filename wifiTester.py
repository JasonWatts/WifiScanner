#!/usr/bin/env python3
import pyspeedtest, requests, json
from merakiJsonHandler import MerakiJsonHandler

class wifiTester(object):
    def __init__(self):
        self.ping = none
        self.download = none
        self.upload =  none
        self.wap = none

    def getSpeedtest(self, verbose=True):
        try: # Speed Test  
            st = pyspeedtest.SpeedTest()
            self.ping = round(st.ping(), 2)
            self.download = round(st.download() / 1000000, 2)
            self.upload = round(st.upload() / 1000000, 2)
            if verbose: 
                print("Ping:", ping)
                print("Download:", download)
                print("Upload:", upload)
        except Exception as e:
            print("Speedtest Error:", e)

    def getWapData(self, verbose = True):
        try: # Access Point Data
            self.wap = MerakiJsonHandler()
            if verbose: 
                print("Name:", self.wap.config.node_name)
                # More stuff
                print("rssi:", self.wap.client.rssi)
        except Exception as e:
            print("Meraki Json Error:", e)

