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

worksheet = client.open('GoogleSheet')
sheet = worksheet.sheet1
sheets = worksheet.worksheets()
sheet2 = worksheet.worksheet('Sheet2')
#sheet = client.openall()
#sheet.append_row(['a', '8', 'f'])
# https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html
# https://www.youtube.com/watch?v=7I2s81TsCnc
# https://gspread.readthedocs.io/en/latest/user-guide.html#opening-a-spreadsheet
# sheet.delete_row(2)
# row = ["I'm", "inserting", "a", "row", "into", "a,", "Spreadsheet", "with", "Python"]
# index = 1
# sheet.insert_row(row, index)
# sheet.delete_row(1)
data = sheet.get_all_records()
dataa = sheet.row_values(1)
dataaa = sheet.col_values(1)
cell = sheet.cell(1, 2)
pp.pprint(data)
print(dataa)
print(dataaa)
print(cell)
print(sheet.row_count)
print(sheet.row_values)
print(sheets)
print(sheet2.get_all_records())
