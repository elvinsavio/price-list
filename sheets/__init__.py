import gspread, datetime
from utils import config


class Sheet:
    def __init__(self) -> None:
        self.gc = gspread.service_account(".config/gspread.json")
        self.sh = self.gc.open("Price list")
        self.store = {
            "titles": {
                "timestamp": datetime.datetime.now(),
                "data": [i.title for i in self.sh],
            }
        }

    def get_titles(self):
        age = datetime.datetime.now() - self.store["titles"]["timestamp"]
        if age.total_seconds() > config["cache_time"]:
            self.store["titles"] = {
                "timestamp": datetime.datetime.now(),
                "data": [i.title for i in self.sh],
            }
        return {"data": self.store["titles"]["data"], 'last_updated':self.store["titles"]['timestamp'] }


sheet = Sheet()
