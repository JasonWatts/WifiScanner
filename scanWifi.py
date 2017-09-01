#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyspeedtest

class Results(object):
    def __init__(self):
        self.ping = 0
        self.download = 0
        self.upload = 0

    def scan():
        try:
            st = pyspeedtest.SpeedTest()
            ping = st.ping()
            download = st.download()
            upload = st.upload()
            result = results(ping, download, upload)
            return result
        except:
            print("Error")

    def average(

def main():
    # Requires Editing
    user = "TYPE YOUR USER HERE"
    device = "TYPE YOUR DEVICE HERE"
    driver = "/Users/jamessolum/git/WifiScanner/chromedriver"
    
    # Helpful Sites
    speedTest = "http://www.beta.speedtest.net/"
    survey = "https://docs.google.com/forms/d/e/1FAIpQLSfFh56GV63_CJWpbNEc-K41p6EgdtztOo83Wz9ZssH2i5V9bw/viewform?c=0&w=1"
    meraki = "my.meraki.com"
    dorm = "GLC"
    
    #User input
    print("Wifi Scanner")
    print("User: ", user)
    print("Device: ", device)
    location = dorm + "-" + str(input("Room number:"))
    
     


if __name__ == "__main__":
    main()

    


