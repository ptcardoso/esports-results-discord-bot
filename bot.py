import discord
from discord.ext import commands

from counterstrike.scrapper.ongoing import get_ongoing_matches
from counterstrike.scrapper.results import get_latest_results
from counterstrike.scrapper.upnext import get_up_next_matches
from settings import TOKEN

client = discord.Client()
bot = commands.Bot(command_prefix='!')


@bot.command()
async def results(ctx):
    games = get_latest_results()
    results_text = '```'
    for game in games[:10]:
        team1, results1, team2, results2 = game
        results_text += "{} {} - {} {}\n".format(team1.ljust(20), results1.ljust(2), results2.rjust(2), team2.rjust(20))
    results_text += '```'
    await ctx.send(results_text)


@bot.command()
async def ongoing(ctx):
    games = get_ongoing_matches()
    results_text = ''
    for game in games[:10]:
        team1, team2, stream = game
        results_text += "{} vs {} <{}>\n".format(team1, team2, stream)
    await ctx.send(results_text)


@bot.command()
async def upnext(ctx):
    games = get_up_next_matches()
    results_text = ''
    for game in games[:20]:
        team1, team2, date = game
        if team1 and team2:
            results_text += "{} vs {} - {}\n".format(team1, team2, date)
        elif date:
            results_text += "\n{}\n".format(date)
    await ctx.send(results_text)


bot.run(TOKEN)
