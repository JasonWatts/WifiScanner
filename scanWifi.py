#! /usr/bin/env python3
import argparse
from wifiTester import wifiTester

def getDefaults():
    try: 
        info = open("info.txt","r")
        return info.readlines()
    except Exception as e:
        print("Error with getting saved information:", e)
        print("Try Running Setup")

def handleArgs(defaults):
    parser = argparse.ArgumentParser(description='ATTsn Wifi Scanner.')
    parser.add_argument('-user', default=defaults[1].rstrip('\n'), help='who are you!?')
    parser.add_argument('-location', required=True, help='Dorm or Building')
    parser.add_argument('-device', default=defaults[2].rstrip('\n'), help='The device you are scanning with (i.e. mac or pc)', choices=['mac', 'm', 'pc', 'p'])
    parser.add_argument('-verbose', action='store_true') 
    return parser.parse_args()

def printInfo(verbose, args):
    if verbose:
        print("\nINFO:")
        print("-----------------")
        print("User:", args.user)
        print("Location:", args.location)
        print("Device:", args.device)
        print("-----------------\n")

def main():
    defaults = getDefaults()
    args = handleArgs(defaults)
    tester = wifiTester()
    
    print("Initializing Speed Test")
    printInfo(args.verbose, args)
    tester.getSpeedtest()
    tester.getWapData()


if __name__ == "__main__":
    main()
