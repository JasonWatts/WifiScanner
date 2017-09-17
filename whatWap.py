#!/usr/bin/env python3
from merakiJsonHandler import MerakiJsonHandler
import sys, time

def main():
    i = 0
    while True:
        i += 1
        try: 
            wap = MerakiJsonHandler()
            name = wap.config.node_name
            print(" ", name, i, end = "\r")
            time.sleep(3)
        except KeyError as e:
            print("Not Connected... ", i,  end="\r")
        except KeyboardInterrupt:
            print()
            sys.exit()

if __name__ == "__main__":
    main()

    

