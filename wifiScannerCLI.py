#!/usr/bin/python
import pyspeedtest
import requests
from lxml import html
from bs4 import BeautifulSoup

def main():
    # Requires Editing
    user = "jsolum"
    device = "Mac desktop or laptop"
    driver = "/Users/jamessolum/git/WifiScanner/chromedriver"
    dorm = "GLC"
   
    # Helpful Sites
    meraki = 'http://my.meraki.com/#connection'

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

    # WAP Data
    page = requests.get(meraki)
    content = html.fromstring(page.content)
    soup = BeautifulSoup(content, 'html.parser')
    print(soup.prettify())


if __name__ == "__main__":
    main()

    


