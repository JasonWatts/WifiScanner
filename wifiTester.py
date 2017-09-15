#!/usr/bin/env python3
import time
import calendar
import pyspeedtest
from merakiJsonHandler import MerakiJsonHandler

class WifiTester(object):
    def __init__(self):
        self.verbose = True 
        # Speed Test    
        self.time = 0
        self.ping = 0
        self.download = 0
        self.upload =  0
        # Wap Data 
        self.wap = "unknown"
        self.lat = 0
        self.lng = 0
        self.channel = 0
        self.rssi = 0
        self.utilization = 0
        self.device = "Unknown"

    def timeStamp(self):
        ts = calendar.timegm(time.gmtime())
        self.time = time.ctime(ts)

    def getSpeedtest(self):
        try: # Speed Test  
            st = pyspeedtest.SpeedTest()
            self.ping = pyspeedtest.pretty_speed(st.ping())
            self.download = pyspeedtest.pretty_speed(st.download())
            self.upload = pyspeedtest.pretty_speed(st.upload())
            self.timeStamp() # Set Time stamp after Speed Tests
            if self.verbose: 
                self.printSpeedTestData()
        except Exception as e:
            print("Speedtest Error:", e)

    def getWapData(self):
        try: # Access Point Data
            self.wap = MerakiJsonHandler()
            self.lat = self.wap.config.lat
            self.lng = self.wap.config.lng
            self.channel = self.wap.client.channel
            self.rssi = self.wap.client.rssi 
            self.utilization = self.wap.utilization2()
            self.name= self.wap.config.node_name
            if self.verbose: 
                self.printWapData()
        except Exception as e:
            print("Meraki Json Error:", e)

    def printWapData(self):
        print("\nWAP Data:")
        print("---------------")
        print("Name:", self.name)
        print("Utilization:", self.utilization)
        print("Channel:", self.channel)
        print("RSSI:", self.rssi)
        print("Latitude:", self.lat)
        print("Longitude:", self.lng)

    def printSpeedTestData(self):
        print("Speed Test Data:")
        print("---------------")
        print("Ping:", self.ping)
        print("Download:", self.download)
        print("Upload:", self.upload)
        print(self.time)


