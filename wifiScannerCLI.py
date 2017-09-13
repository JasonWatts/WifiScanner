#!/usr/bin/env python3
import pyspeedtest, requests, json
from merakiJsonHandler import MerakiJsonHandler

def main():
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
        print("Ping:", ping)
        print("Download:", download)
        print("Upload:", upload)
    except Exception as e:
        print("Speedtest Error:", e)

    try: # Access Point Data
        wap = MerakiJsonHandler()
        print("Name:", wap.config.node_name)
        print("rssi:", wap.client.rssi)
    except Exception as e:
        print("Meraki Json Error:", e)


if __name__ == "__main__":
    main()

    


