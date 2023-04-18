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
  if message.author.id == "1096017556415987762": return

  if message.content.lower().startswith("!db "):
    str = ""

    tar = "html"

    search_word = message.content.lower().replace("!db", "")

    pages_num = 3 + 1

    search_word1 = search_word + "site:battlecats-db.com/"

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
      idx = site_url.find(tar)
      site_url2 = site_url[:idx + 4]
      str += site_title + "\n" + site_url2 + "\n"
    embed = discord.Embed(title=f'【検索ワード】{search_word}',
                          description=str,
                          color=discord.Colour.yellow())
    await message.channel.send(embed=embed)
    

client.run("TOKEN")
