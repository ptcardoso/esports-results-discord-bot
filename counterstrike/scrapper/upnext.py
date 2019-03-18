from bs4 import BeautifulSoup
from counterstrike.scrapper.settings import BASE_URL, UP_NEXT_PATH
from network.http import simple_get
from datetime import datetime

UP_NEXT_URL = "{}{}/".format(BASE_URL, UP_NEXT_PATH)


def get_up_next_matches():
    raw_results = simple_get(UP_NEXT_URL)
    results = BeautifulSoup(raw_results, 'html.parser')

    time = results.select('div.match-day a tr td.time div.time')
    team1_html = results.select('div.match-day a tr td.team-cell div.team')
    team2_html = results.select('div.match-day a tr td.vs + td.team-cell div.team')

    games_html = list(zip(team1_html, team2_html, time))
    games = []
    current_day = ''
    for game_html in games_html:
        team1 = game_html[0].text
        team2 = game_html[1].text
        date_unix = int(game_html[2]['data-unix'])/1000
        day = datetime.utcfromtimestamp(date_unix).strftime('%Y-%m-%d')
        if day != current_day:
            current_day = day
            games.append((None, None, day))
        time = datetime.utcfromtimestamp(date_unix).strftime('%H:%M (UTC)')
        games.append((team1, team2, time))

    return games
