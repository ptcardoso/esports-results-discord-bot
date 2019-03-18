from bs4 import BeautifulSoup
from counterstrike.scrapper.settings import BASE_URL, RESULTS_PATH
from network.http import simple_get

RESULTS_URL = "{}{}/".format(BASE_URL, RESULTS_PATH)


def get_latest_results():
    raw_results = simple_get(RESULTS_URL)
    results = BeautifulSoup(raw_results, 'html.parser')

    team1_html = results.select('tr td.team-cell div.team1 div.team')
    result1_html = results.select('tr td.result-score span:first-child')
    team2_html = results.select('tr td.team-cell div.team2 div.team')
    result2_html = results.select('tr td.result-score span:last-child')

    games_html = list(zip(team1_html, result1_html, team2_html, result2_html))
    games = []
    for game_html in games_html:
        team1 = game_html[0].text
        result1 = game_html[1].text
        team2 = game_html[2].text
        result2 = game_html[3].text
        games.append((team1, result1, team2, result2))

    return games
