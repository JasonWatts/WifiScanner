#!/usr/bin/env python3
import gspread
from oauth2client.service_account import ServiceAccountCredentials

SHEET_KEY = "1pTHKzoJyq2UZMBQduGyoRLtxdzcu4ITEvBv48TEaKwE"

scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
gc = gspread.authorize(credentials)

sheet = gc.open_by_key(SHEET_KEY).sheet1

row = ["hello", "my", "name", "is", "James", 4]
sheet.insert_row(row, sheet.row_count+1)
