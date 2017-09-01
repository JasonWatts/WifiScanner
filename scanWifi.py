#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyspeedtest

class Scanner(object):
    def __init__(self):
        self.listPing = []
        self.listDownload = []
        self.listUpload = []

    def scan():
        try:
            st = pyspeedtest.SpeedTest()
            ping = st.ping()
            download = st.download()
            upload = st.upload()

            listPing.append(ping)
            listDownload.append(download)
            listUpload.append(upload)
        except:
            print("Error")

    def average(aList):
		total = 0
		for num in aList:
			total = total + num 
		return total/len(aList)


    def fullScan(num):
    	for n in range(num):
    		scan()

    	print("Ping: ", average(listPing))
    	print("Download: ", average(listDownload))
    	print("Upload: ", average(listUpload))










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

    


