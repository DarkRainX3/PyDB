import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
pp = pprint.PrettyPrinter()
# pip install PyOpenSSL
# pip install --upgrade google-api-python-client oauth2client
# pip install gspread

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('manager.json', scope)
client = gspread.authorize(creds)

sheet = client.open('GoogleSheet').sheet1
#sheet = client.openall()
sheet.append_row(['a', '123412', 'word'])
# https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html
# https://www.youtube.com/watch?v=7I2s81TsCnc
# sheet.delete_row(2)
#data = sheet.get_all_records()
# print(data)
