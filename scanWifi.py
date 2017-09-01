#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyspeedtest

class Scanner(object):
    def __init__(self):
        self.avgPing = 0
        self.avgDownload = 0
        self.avgupload =0
        self.listPing = []
        self.listDownload = []
        self.listUpload = []

    def scan(self):
        try:
            st = pyspeedtest.SpeedTest()
            ping = st.ping()
            download = st.download()
            upload = st.upload()

            listPing.append(ping)
            listDownload.append(download)
            listUpload.append(upload)
        except:
            print("Error with Scan")

    def average(aList):
        total = 0
        for num in aList:
            total = total + num 
        return total/len(aList)

    def fullScan(self, num):
        for n in range(num):
            self.scan()
        self.avgPing = (average(listPing))
        print("Ping: ", self.avgPing)
        self.avgDownload = (average(listDownload))
        print("Download: ", self.avgDownload)
        self.avgUpload = (average(listUpload))
        print("Upload: ", self.avgUpload)

def main():
    # Requires Editing
    user = "TYPE YOUR USER HERE"
    device = "TYPE YOUR DEVICE HERE"
    driver = "/Users/jamessolum/git/WifiScanner/chromedriver"
    dorm = "GLC"
   
    # Helpful Sites
    speedTest = "http://www.beta.speedtest.net/"
    survey = "https://docs.google.com/forms/d/e/1FAIpQLSfFh56GV63_CJWpbNEc-K41p6EgdtztOo83Wz9ZssH2i5V9bw/viewform?c=0&w=1"
    meraki = "my.meraki.com"
    scanSize = 1

    #User input
    print("Wifi Scanner")
    print("User: ", user)
    print("Device: ", device)
    location = dorm + "-" + str(input("Room number:"))
  
    scanner = Scanner()
    scanner.fullScan(scanSize)
    
    browser = webdriver.Chrome(driver)
    browser.get(meraki)
    deviceName = browser.find_element_by_name('device_name').text
    print("Device name: ", deviceName)


if __name__ == "__main__":
    main()

    


