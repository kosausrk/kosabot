import discord
import json
import random
import requests
from bs4 import BeautifulSoup
from googleapiclient.discovery import build
client = discord.Client()
#youtube api
api_key = "AIzaSyDUk3rQ8sg_2qau3r9fWGeLX_cbgN6mOug"
youtube = build("youtube", "v3", developerKey = api_key)
pewdiepie = youtube.channels().list(part= "statistics", forUsername = "PewDiePie")
youtube_data = pewdiepie.execute()
pewdiepie_subcount = youtube_data['items'][0]['statistics']['subscriberCount']
print("PewDiePie currently has: "+ pewdiepie_subcount + "subscribers")
david_dobrik = youtube.channels().list(part= "statistics", id = "UCmh5gdwCx6lN7gEC20leNVA")
youtube_data2 = david_dobrik.execute()
david_dobrik_subcount = youtube_data['items'][0]['statistics']['subscriberCount']
print(youtube_data2)
#tesla
url = requests.get("https://www.marketwatch.com/investing/stock/tsla")
soup = BeautifulSoup(url.content, 'html.parser')
content = soup.find("bg-quote", {"class" : "value"}, {"session" : "pre"})
tesla = content.get_text()
#apple
url2 = requests.get("https://www.marketwatch.com/investing/stock/aapl")
soup2 = BeautifulSoup(url2.content, "html.parser")
content2 = soup2.find("bg-quote", {"class" : "value"})
apple = content2.get_text()
#google
url3 = requests.get("https://www.marketwatch.com/investing/stock/googl")
soup3 = BeautifulSoup(url3.content, "html.parser")
content3 = soup3.find("bg-quote", {"class": "value"})
google = content3.get_text()
#bths
url4 = requests.get("https://bths.edu")
soup4 = BeautifulSoup(url4.content, "html.parser")
content4 = soup4.find("div", {"role": "group"})
bths_today = content4.get_text()
bths_today = " ".join(bths_today.split())
print(bths_today)
print(bths_today)
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]["q"] + " -" + json_data[0]["a"]
  return quote

hello_list = ["NO, not hello you faggot no one wants to talk to you", "Hello? More like please shut the fuck up", "Hello!?!? Do the world a favor and search up 24 oz bleach on amazon and chug it "]

starter_encouragements = ["Kill yourself", "Please just die", "Just do it, better for everyone", "Go KYS kid", "Fuck you soggy peice of stale bread", "Waste of chemicals headass"
]
@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith("$david dobrik"):
    await message.channel.send("David Dobrik has " + david_dobrik_subcount)
  if message.content.startswith("$today"):
    await message.channel.send("Today is: " + bths_today)
  if message.content.startswith("$google"):
    await message.channel.send("Current price of google is " + "$" + google)
  if message.content.startswith("$apple"):
    await message.channel.send("Current price of apple stock is " + "$" + apple)
  if message.content.startswith("$help"):
    await message.channel.send("Commands: $inspire, $hello, jew, $tesla, $apple, $google and $happy")
  if message.content.startswith("$happy"):
    await message.channel.send(random.choice(starter_encouragements))
  if message.content.startswith("$tesla"):
    await message.channel.send("Current price of tesla stock is: " + "$" + tesla)
  if message.content.startswith("$inspire"):
    quote = get_quote()
    await message.channel.send(quote)
  if message.content.startswith("$hello"):
    await message.channel.send(random.choice(hello_list))
  if message.content.startswith("jew"):
    await message.channel.send("JEW NIGGER FAGGOT SHUT UP")
client.run("Nzc5NzU5Njc0MDEwMTA3OTk2.X7lNyQ.e2v8tEonRl1m-gQluHWNhV8ohyY")