import gspread, datetime
from utils import config
from thefuzz import process


class Sheet:
    def __init__(self) -> None:
        self.gc = gspread.service_account(".config/gspread.json")
        self.sh = self.gc.open("Price list")
        self.store = {
            "titles": {
                "timestamp": datetime.datetime.now(),
                "data": [i.title for i in self.sh],
            },
            "data": {},
        }

    def _update_cached_title(self):
        age = datetime.datetime.now() - self.store["titles"]["timestamp"]
        if age.total_seconds() > config["cache_time"]:
            self.store["titles"] = {
                "timestamp": datetime.datetime.now(),
                "data": [i.title for i in self.sh],
            }

    def _update_cached_data(self, title):
        try:
            age = datetime.datetime.now() - self.store["data"][title]["timestamp"]
            if age.total_seconds() > config["cache_time"]:
                self.store["data"][title] = {
                    "timestamp": datetime.datetime.now(),
                    "data": [
                        {"name": i[1], "price": i[2]}
                        for i in self.sh.worksheet(title).get_all_values()[1:]
                    ],
                }
        except Exception:
            self.store["data"][title] = {
                "timestamp": datetime.datetime.now(),
                "data": [
                    {"name": i[1], "price": i[2]}
                    for i in self.sh.worksheet(title).get_all_values()[1:]
                ],
            }

    def search_title(self, search_term):
        self._update_cached_title()
        found_match = []
        results = process.extract(search_term, self.store["titles"]["data"])
        for result in results:
            if result[1] >= 80:
                found_match.append(result[0])
        return {
            "data": found_match,
            "last_updated": self.store["titles"]["timestamp"],
        }

    def get_titles(self):
        self._update_cached_title()
        age = datetime.datetime.now() - self.store["titles"]["timestamp"]
        if age.total_seconds() > config["cache_time"]:
            self.store["titles"] = {
                "timestamp": datetime.datetime.now(),
                "data": [i.title for i in self.sh],
            }
        return {
            "data": self.store["titles"]["data"],
            "last_updated": self.store["titles"]["timestamp"],
        }

    def get_list_items(self, title):
        self._update_cached_data(title)
        return self.store["data"][title]


sheet = Sheet()
