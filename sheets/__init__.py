import gspread
from utils import config

class Sheet:
    def __init__(self) -> None:
        self.gc = gspread.service_account(".config/gspread.json")
        self.sh = self.gc.open("Price list")


    def get_titles(self):
        result = []
        for i in self.sh:
            result.append(i.title)
        return result


sheet = Sheet()
