#!/usr/bin/env python3
import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials

class SheetsController(object):
    def __init__(self, url=None):
        self.scope = ['https://spreadsheets.google.com/feeds']
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', self.scope)
        self.row = None
        if url == None:
            try: 
                with open('info.json') as data_file:    
                    data = json.load(data_file)
                    self.sheetUrl = data['url'] 
            except Exception as e:
                print("Error with getting Sheet Url:", e)
        else:
            self.sheetUrl = url
    
    def authorize(self):
        return gspread.authorize(self.credentials)

    def uploadData(self, data):
        gc = gspread.authorize(self.credentials)
        sheet = gc.open_by_url(self.sheetUrl).sheet1
        try:
            sheet.insert_row(data, sheet.row_count+1)
            print("Data Sent!\n")
        except Exception as e:
            print("Error with writing data:", e)
