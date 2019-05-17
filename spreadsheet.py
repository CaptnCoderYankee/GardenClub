import gspread
from oauth2client.service_account import ServiceAccountCredentials
import temp_Detection

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open("Temperatures").sheet1
print(sheet.get_all_records())

sheet.append_row([temp_Detection.data1, temp_Detection.data2])
