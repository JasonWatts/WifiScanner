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
signal db
'''

def main():
    # Requires Editing
    user = "jsolum"
    device = "Mac desktop or laptop"
    driver = "/Users/jamessolum/git/WifiScanner/chromedriver"
    dorm = "GLC"
   
    # Helpful Sites
    meraki = 'http://my.meraki.com/#connection'
    merakiJson= 'http://my.meraki.com/index.json?t=*'
    wap = requests.get(merakiJson).json()
    node_name = wap['config']['node_name']
'''
    #User input
    print("Wifi Scanner")
    print("User: ", user)
    print("Device: ", device)
    location = dorm + "-" + str(input("Room number: "))
   
    # Speed Test
    st = pyspeedtest.SpeedTest()
    ping = round(st.ping(), 2)
    download = round(st.download() / 1000000, 2)
    upload = round(st.upload() / 1000000, 2)

    print("Ping: ", ping)
    print("Download: ", download)
    print("Upload: ", upload)
'''
    # WAP Data
    

if __name__ == "__main__":
    main()

    


