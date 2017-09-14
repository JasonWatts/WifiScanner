#!/usr/bin/env python3
import pyspeedtest, requests, json
from merakiJsonHandler import MerakiJsonHandler

class wifiTester(object):
    def __init__(self):
        self.verbose = True
        self.ping = None
        self.download = None
        self.upload =  None
        self.wap = None

    def getSpeedtest(self):
        try: # Speed Test  
            st = pyspeedtest.SpeedTest()
            self.ping = round(st.ping(), 2)
            self.download = round(st.download() / 1000000, 2)
            self.upload = round(st.upload() / 1000000, 2)
            if self.verbose: 
                print("Ping:", self.ping)
                print("Download:", self.download)
                print("Upload:", self.upload)
        except Exception as e:
            print("Speedtest Error:", e)

    def getWapData(self):
        try: # Access Point Data
            self.wap = MerakiJsonHandler()
            if self.verbose: 
                print("Name:", self.wap.config.node_name)
                # More stuff
                print("rssi:", self.wap.client.rssi)
        except Exception as e:
            print("Meraki Json Error:", e)

