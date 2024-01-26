import gspread
import csv, os, datetime
from utils import config

class Sheet:
    def __init__(self) -> None:
        self.gc = gspread.service_account(".config/gspread.json")
        self.sh = self.gc.open("Price list")
        self.file_name = {"history": "./store/hist.csv", "title": "./store/titles.csv"}

        if not os.path.isfile(self.file_name["history"]):
            with open(self.file_name["history"], mode="w", newline="", encoding="utf-8") as hist_file:
                writer = csv.writer(hist_file)
                writer.writerow(["age", "title"]) 

    def _check_age(self, coll: str) -> bool:
        '''
            Check how old an entry is in the coll,
            if older than config['cache_time'] - current time returns False
            else return True

            if cache time is 10 and current is 10:30 -> 10:20 

            args:
                coll: str -> name to query

            return: 
                boolean
        '''
        current_time = datetime.datetime.now()
        cache_time = datetime.timedelta(hours=config['cache_time'])

        with open(self.file_name['history'], mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            for line in reader:
                print(line, coll)
                if len(line) == 2 and line[1] == coll:
                    timestamp = datetime.datetime.strptime(line[0], '%Y-%m-%d %H:%M:%S')
                    if timestamp < current_time - cache_time:
                        return False
                    return True
            return False
        
    def _write_coll(self, title: str, data: any):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        with open(self.file_name['history'], mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            rows = list(reader)

        title_found = False
        for row in rows:
            if len(row) == 2 and row[1] == title:
                title_found = True
                break

        if not title_found:
            rows.append([timestamp, title])

        with open(self.file_name['history'], mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

    def get_titles(self):
        is_old =  self._check_age("titles")
        print(is_old)


        # if not self._check_age("hist"):
        #     self._write_coll('titles', '')

        result = []
        for i in self.sh:
            result.append(i.title)
        return result


sheet = Sheet()
