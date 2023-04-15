import discord
import requests
from bs4 import BeautifulSoup

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("ready!")
    print(discord.__version__)


@client.event
async def on_message(message):
     if message.author.bot:
        return 
     if "!db" in message.content:
         str = ""

         search_word = message.content.replace("!db ", "")

         pages_num = 3 + 1

         search_word1 = "にゃんこ大戦争DB " + search_word

         url = f'https://www.google.co.jp/search?hl=ja&num={pages_num}&q={search_word1}'
         request = requests.get(url)

         soup = BeautifulSoup(request.text, "html.parser")
         search_site_list = soup.select('div.kCrYT > a')

         for rank, site in zip(range(1, pages_num), search_site_list):
             try:
                 site_title = site.select('h3.zBAuLc')[0].text
             except IndexError:
                 site_title = site.select('img')[0]['alt']
             site_url = site['href'].replace('/url?q=', '')
             site_url1 = "https://www.google.co.jp/url?esrc=s&q=&rct=j&sa=U&url=" + site_url
             str += site_title + ": " + site_url1 + "\n"
         embed = discord.Embed(title=f'【検索ワード】{search_word}',description=str)
         await message.channel.send(embed=embed)
 
client.run("MTA5NjAxNzU1NjQxNTk4Nzc2Mg.GI1WVQ.HUvgZv87iMVr3Gj5aDagDBgl91OYfIse46NYaA")
