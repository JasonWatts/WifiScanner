#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyspeedtest

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
    
    #Start Scan
    print("Scan starting!")
    st = pyspeedtest.SpeedTest()
    ping = st.ping()
    print("Ping: ", ping)
    download = st.download()
    print("Download: ", download)
    upload = st.upload()
    print("Upload: ", upload)



if __name__ == "__main__":
    main()

    


