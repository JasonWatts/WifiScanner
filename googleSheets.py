#!/usr/bin/env python3
import gspread
from oauth2client.service_account import ServiceAccountCredentials

class sheetsController(object):
    def __init__(self, url):
        self.scope = ['https://spreadsheets.google.com/feeds']
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
        self.row = None
        self.sheetUrl = url

    def __init__(self):
        self.scope = ['https://spreadsheets.google.com/feeds']
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
        self.row = None
        try:  
            with open('url.txt', 'r') as myfile:
                self.sheetUrl = myfile.read()
        except Exception as e:
            print("Error with getting Sheet Url:", e)
    
    def authorize(self):
        return gspread.authorize(self.credentials)

    def addData(self, data):
        gc = gspread.authorize(self.credentials)
        gc.open_by_url(self.sheetUrl).sheet1
        try:
            sheet.insert_row(data, sheet.row_count+1)
        except Exception as e:
            print("Error with writing data:", e)
        




