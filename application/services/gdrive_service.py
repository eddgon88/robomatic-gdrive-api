import gspread
import os
from dotenv import load_dotenv
from .. models.models import GsheetRequest

load_dotenv()

google_conf = {
    "CLIENT_ID_JSON" : os.getenv('SA_CLIENT_ID'),
    "SCOPES": [
        "https://www.googleapis.com/auth/drive"
        ]
}

class GdriveService:
    def __init__(self):
        self.sa = gspread.service_account(filename=os.getenv('SA_CLIENT_ID'))

    def get_gsheet(self, sheet_config: GsheetRequest):
        print("Getting the Gsheet - " + sheet_config.file_id)
        gs = self.sa.open_by_key(sheet_config.file_id)
        print("Getting the Worksheet - " + sheet_config.sheet_name)
        wks = gs.worksheet(sheet_config.sheet_name)
        print("Getting the range - " + sheet_config.range)
        print(wks.get(sheet_config.range))
        return wks.get(sheet_config.range)