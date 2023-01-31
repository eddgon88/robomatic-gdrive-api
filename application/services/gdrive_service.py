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
        gs = self.sa.open(sheet_config.file_id)
        wks = gs.worksheet(sheet_config.sheet_name)
        return wks.get(sheet_config.range)