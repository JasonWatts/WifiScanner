#!/usr/bin/python
import pyspeedtest
import requests
import json
from lxml import html
'''
speed
access point name
utilization
channel
signal db == rssi
'''

def scan():
    try:  
        st = pyspeedtest.SpeedTest()
        ping = round(st.ping(), 2)
        download = round(st.download() / 1000000, 2)
        upload = round(st.upload() / 1000000, 2)

        print("Ping: ", ping)
        print("Download: ", download)
        print("Upload: ", upload)
    except RuntimeError as e:
        print("Error: ", e)

def main():
    # Helpful Sites
    meraki = 'http://my.meraki.com/#connection'
    merakiJson= 'http://my.meraki.com/index.json?t=*'
   
   # Requires Editing
    user = "jsolum"
    device = "Mac desktop or laptop"

    #User input
    print("Wifi Scanner")
    print("User: ", user)
    print("Device: ", device)
    dorm = str(input("Dorm: "))
    location = dorm + "-" + str(input("Room number: "))
   
    scan() 

    # WAP Data
    try: 
        wap = requests.get(merakiJson).json()
        wapName = wap['config']['node_name']
        # utilization = wap[  NOT SURE WHAT THIS IS
        # channel =  NOT SURE WHAT THIS IS
        signalDb = wap['client']['rssi']
        print("Access Point: ", wapName)
        print("rssi: ", signalDb)
    except:
        print("ERROR: ", wap)
        
if __name__ == "__main__":
    main()

    


