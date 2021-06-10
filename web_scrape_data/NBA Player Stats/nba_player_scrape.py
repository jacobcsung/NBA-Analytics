import requests
import pandas as pd

#Header data
header = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.5",
    "cache-control": "max-age=0",
    "connection": "keep-alive",
    "host": "stats.nba.com",
    "if-modified-since": "Tue, 08 Jun 2021 16:01:22 GMT",
    "origin": "https://www.nba.com",
    "referer": "https://www.nba.com/stats/players/traditional/?PerMode=Totals&sort=PTS&dir=-1",
    "user-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0",
    "x-nba-stats-origin": "stats",
    "x-nba-stats-token": "true"
    }

def get_player_stats(url):
    r = requests.get(url, headers=header).json()
    results = r['resultSets'][0]
    headers = results['headers']
    rows = results['rowSet']
    data_frame = pd.DataFrame(rows)
    data_frame.columns = headers
    return data_frame

def player_stats_url(season, type):
    return 'https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season={0}&SeasonSegment=&SeasonType={1}&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight='.format(season, type)

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
        df = get_player_stats(player_stats_url(season, type))
        df.to_csv("{0}_{1}_nba_player_stats".format(season, type), index = False)

