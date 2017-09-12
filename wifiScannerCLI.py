#!/usr/bin/python
import pyspeedtest
import requests
import json
from lxml import html

def main():
    meraki= 'http://my.meraki.com/index.json?t=*'
    user = "jsolum"
    device = "Mac desktop or laptop"

    # User input
    print("Wifi Scanner")
    print("User: ", user)
    print("Device: ", device)
    dorm = str(input("Dorm: "))
    location = dorm + "-" + str(input("Room number: "))

    try: # Speed Test  
        st = pyspeedtest.SpeedTest()
        ping = round(st.ping(), 2)
        download = round(st.download() / 1000000, 2)
        upload = round(st.upload() / 1000000, 2)
        
        #print("Ping:", ping)
        #print("Download:", download)
        #print("Upload:", upload)
    except Exception:
        print("ERROR: speedtest failed")

    try: # Access Point Data
        wap = requests.get(meraki).json()
        wapName = wap['config']['node_name']
        signalDb = wap['client']['rssi']
        print("Access Point: ", wapName)
        print("rssi: ", signalDb)
    except:
        print("ERROR: can't connect to access point")

    '''
    prof_rc = wap['radio_stats'][0]['prof_rc']
    print(prof_rc)
    prof_cc = wap['radio_stats'][0]['prof_cc']
    print(prof_cc)
    answer = (100* prof_rc)/prof_cc
    print("Utilization:", answer)
    '''
        
if __name__ == "__main__":
    main()

    


