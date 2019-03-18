from bs4 import BeautifulSoup
from counterstrike.scrapper.settings import BASE_URL, MATCHES_PATH
from network.http import simple_get

MATCHES_URL = "{}{}/".format(BASE_URL, MATCHES_PATH)


def get_match_detail(path):
    match_detail_url = "{}{}/".format(BASE_URL, path)
    raw_match_detail = simple_get(match_detail_url)
    match_detail = BeautifulSoup(raw_match_detail, 'html.parser')
    stream_anchors = match_detail.select('div.streams div.external-stream a')
    return [stream_anchor['href'] for stream_anchor in stream_anchors]


def get_ongoing_matches():
    raw_results = simple_get(MATCHES_URL)
    matches = BeautifulSoup(raw_results, 'html.parser')
    team1_html = matches.select('div.live-match div.scores tr:nth-child(2) td.teams span.team-name')
    team2_html = matches.select('div.live-match div.scores tr:nth-child(3) td.teams span.team-name')
    detail_url = matches.select('div.live-match > a:first-child')
    stream_urls = get_match_detail(detail_url[0]['href'])
    games_html = list(zip(team1_html, team2_html, stream_urls))
    games = []
    for game_html in games_html:
        team1 = game_html[0].text
        team2 = game_html[1].text

        games.append((team1, team2, game_html[2]))

    return games
