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
   

#Class containing helper functions to scrape specific NBA data
class nbaScraper(Scraper):

    def __init__(self, init_header):
        super().__init__(init_header)

    #Helper function that returns the player stats page given a certain season and season type
    def player_stats_url(season, type):
        return 'https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season={0}&SeasonSegment=&SeasonType={1}&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight='.format(season, type)

    #Helper Function for season games
    def season_stat_url(season, type):
        return "https://stats.nba.com/stats/leaguegamelog?Counter=1000&DateFrom=&DateTo=&Direction=DESC&LeagueID=00&PlayerOrTeam=T&Season={0}&SeasonType={1}&Sorter=DATE".format(season, type)

    #Helper function for team data
    def game_team_url(season, type):
        return "https://stats.nba.com/stats/leaguedashteamstats?Conference=&DateFrom=&DateTo=&Division=&GameScope=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season={0}&SeasonSegment=&SeasonType={1}&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=".format(season, type)




#scrape = Scraper(player_header)

#df = scrape.scrape(player_stats_url(SEASON, TYPE))
#df.to_csv("test", index = False)

#Example script used to scrape all data:

# seasons = [
#    '1996-97',
#    '1997-98',
#    '1998-99',
#    '1999-00',
#    '2000-01',
#    '2001-02',
#    '2002-03',
#    '2003-04',
#    '2004-05',
#    '2005-06',
#    '2006-07',
#    '2007-08',
#    '2008-09',
#    '2009-10',
#    '2010-11',
#    '2011-12',
#    '2012-13',
#    '2013-14',
#    '2014-15',
#    '2015-16',
#    '2016-17',
#    '2017-18',
#    '2018-19',
#    '2019-20',
#    '2020-21',]

# types = ["Regular+Season", "Playoffs"]

# HEADER_SEASON = {
#    "Accept": "application/json, text/plain, */*",
#    "Accept-Encoding": "gzip, deflate, br",
#    "Accept_Language": "en-US,en;q=0.5",
#    "Connection" : "keep-alive",
#    "Host": "stats.nba.com",
#    "Origin": "https://www.nba.com",
#    "Referer": "https://www.nba.com/stats/teams/boxscores/",
#    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0",
#    "x-nba-stats-origin": "stats",
#    "x-nba-stats-token" : "true"
#}

#Suppose we wanted to get seasonal data for these specific seasons as well as these specific season types:

# nba_scrape = nbaScraper(HEADER_SEASON)

#for season in seasons:
#    for type in types:
#        df = nba_scrape.scrape(nba_scrape.season_stat_url(season,type))
#        df.to_csv("{0}_{1}_season_stats".format(season, type), index = False)
