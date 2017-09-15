#! /usr/bin/env python3
import argparse
import json
from wifiTester import WifiTester
from googleSheets import SheetsController

def getDefaults():
    try: 
        with open('info.json') as data_file:    
            return json.load(data_file)
    except Exception as e:
        print("No default data available.  Run Setup to configure:", e)
        return {'user':'unknown','url':'unknown','device':'unknown'}

def handleArgs():
    defaults = getDefaults()
    parser = argparse.ArgumentParser(description='ATTsn Wifi Scanner.')
    parser.add_argument('-user', default=defaults['user'], help='who are you!?')
    parser.add_argument('-location', required=True, help='Dorm or Building')
    parser.add_argument('-room', help='Room number. Will be appended to location')
    parser.add_argument('-device', default=defaults['device'], help='The device you are scanning with (i.e. Mac or PC)', choices=['Mac', 'Pc'])
    parser.add_argument('-loop', help='Allows you to repeat Wifi Scans.', action='store_true')
    parser.add_argument('-noRoom', help='Prevents Room prompt.', action='store_true')
    parser.add_argument('-verbose', action='store_true') 
    return parser.parse_args()

def printInfo(args):
    print("\nINFO:")
    print("-----------------")
    print("User:", args.user)
    print("Location:", args.location)
    print("Device:", args.device)
    print("-----------------\n")

def prepareData(myWifiTester, args, notes):
    return [myWifiTester.time, myWifiTester.name, args.location, myWifiTester.upload, myWifiTester.download, myWifiTester.ping, myWifiTester.lat, myWifiTester.lng, myWifiTester.channel, myWifiTester.rssi, myWifiTester.utilization, args.device, args.user, notes]

def main():
    args = handleArgs()
    if not args.room == None:
        args.location = args.location + "-" + args.room
    tester = WifiTester()
    googleSheets = SheetsController()
    print("\nSpeed Test Initialized")
    printInfo(args)
    while True:
        tester.getSpeedtest()
        tester.getWapData()
        notes = input("\nNotes: ")
        data = prepareData(tester, args, notes)
        googleSheets.uploadData(data)
        if args.loop:
            print("----------------------\n")
            answer = input("Start new speed test? (y/n): ")
            if answer == "y":
                print("\nStarting new wifi Test with previous Settings")
                if (not args.room == None) :
                    args.room = input("\nRoom: ")
                    args.location = args.location.split('-', 1)[0]
                    args.location = args.location + "-" + args.room
                    print("Location:", args.location, "\n")
            else: 
                break
        else:
            break

if __name__ == "__main__":
    main()
