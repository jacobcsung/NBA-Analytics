# Web Scraping Object Oriented approach
import requests
import pandas as pd

class Scraper:

    def __init__(self, init_header):
        self._header = init_header

    #Returns object header for scrpaing
    @property
    def header(self):
        return self._header

    #Setting the header
    @header.setter
    def header(self, new_head):
        if not isinstance(new_head, dict):
            raise TypeError("Header must be a Dictionary.")
        self._header = new_head

    #Scrapes webpage, returns data as a Pandas DataFrame    
    def scrape(self, url):
        r = requests.get(url, headers=self.header).json()
        results = r['resultSets'][0]
        headers = results['headers']
        rows = results['rowSet']
        data_frame = pd.DataFrame(rows)
        data_frame.columns = headers
        return data_frame
   





#Example Code:

#player_header = {
 #   "accept": "application/json, text/plain, */*",
 #   "accept-encoding": "gzip, deflate, br",
 #   "accept-language": "en-US,en;q=0.5",
 #   "cache-control": "max-age=0",
 #   "connection": "keep-alive",
 #   "host": "stats.nba.com",
 #   "if-modified-since": "Tue, 08 Jun 2021 16:01:22 GMT",
 #   "origin": "https://www.nba.com",
 #   "referer": "https://www.nba.com/stats/players/traditional/?PerMode=Totals&sort=PTS&dir=-1",
 #   "user-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0",
 #   "x-nba-stats-origin": "stats",
 #   "x-nba-stats-token": "true"
 #   }

# SEASON = '2020-21'
# TYPE = "Playoffs"

#def player_stats_url(season, type):
#    return 'https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season={0}&SeasonSegment=&SeasonType={1}&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight='.format(season, type)

#scrape = Scraper(player_header)

#df = scrape.scrape(player_stats_url(SEASON, TYPE))
#df.to_csv("test", index = False)