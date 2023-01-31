import gspread

google_conf = {
    "CLIENT_ID_JSON" : "/home/edgar/robomatic/angular-theorem-365416-c6cdce323288.json",
    "SCOPES": [
        "https://www.googleapis.com/auth/drive"
        ]
}

class GdriveService:
    def __init__(self):
        self.sa = gspread.service_account(filename="/home/edgar/robomatic/angular-theorem-365416-c6cdce323288.json")

    def get_gsheet(self, sheet_config):
        print("Getting the Gsheet - " + sheet_config.file_id)
        gs = self.sa.open(sheet_config.file_id)
        print("Getting the Worksheet - " + sheet_config.sheet_name)
        wks = gs.worksheet(sheet_config.sheet_name)
        print("Getting the range - " + sheet_config.range)
        print(wks.get(sheet_config.range))
        return wks.get(sheet_config.range)