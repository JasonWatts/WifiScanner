#!/usr/bin/python
import requests
from bs4 import BeautifulSoup

try: 
    meraki = 'http://my.meraki.com/#connection'
    page = requests.get(meraki, timeout= 1)
except:
    print("Error: Bad URL")
    exit()

try:
    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup.prettify())
except:
    print("Error: ", page.status_code)

deviceName = soup.find_all(id="device_name")[0]
print("Device: ", deviceName.get_text())

