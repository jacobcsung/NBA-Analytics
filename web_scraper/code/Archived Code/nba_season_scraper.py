import requests
import time
import pandas as pd

header = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept_Language": "en-US,en;q=0.5",
    "Connection" : "keep-alive",
    "Host": "stats.nba.com",
    "Origin": "https://www.nba.com",
    "Referer": "https://www.nba.com/stats/teams/boxscores/",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0",
    "x-nba-stats-origin": "stats",
    "x-nba-stats-token" : "true"
}

def get_season_stats(url):
    r = requests.get(url, headers=header).json()
    results = r['resultSets'][0]
    headers = results['headers']
    rows = results['rowSet']
    data_frame = pd.DataFrame(rows)
    data_frame.columns = headers
    return data_frame

def season_stat_url(season, type):
    return "https://stats.nba.com/stats/leaguegamelog?Counter=1000&DateFrom=&DateTo=&Direction=DESC&LeagueID=00&PlayerOrTeam=T&Season={0}&SeasonType={1}&Sorter=DATE".format(season, type)

#Contains NBA seasons
seasons = [
    '1996-97',
    '1997-98',
    '1998-99',
    '1999-00',
    '2000-01',
    '2001-02',
    '2002-03',
    '2003-04',
    '2004-05',
    '2005-06',
    '2006-07',
    '2007-08',
    '2008-09',
    '2009-10',
    '2010-11',
    '2011-12',
    '2012-13',  
    '2013-14',
    '2014-15',
    '2015-16',
    '2016-17',
    '2017-18',
    '2018-19',
    '2019-20',
    '2020-21',]

#Season type (Only interested in data during regular season and playoffs)
types = ["Regular+Season", "Playoffs"]

for season in seasons:
    for type in types:
        time.sleep(5)
        df = get_season_stats(season_stat_url(season, type))
        df.to_csv("{0}_{1}_season_stats".format(season, type), index = False)