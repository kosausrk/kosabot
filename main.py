import discord
import os
import json
import random
import requests
from bs4 import BeautifulSoup
from replit import db
from googleapiclient.discovery import build
from keep_alive import keep_alive



client = discord.Client()
#news   
url6 = requests.get("https://www.nydailynews.com")
soup6 = BeautifulSoup(url6.content, "html.parser")
headline2 = soup6.find("a",{"class":"no-u"})
headline2_description  = soup6.find("div", {"data-pb-field": "description.basic"})
headline3 = soup6.find("h2", {'class': "r-mb h6"})
headline4 = soup6.find("p", {"class": "r-mb h6"})


url5 = requests.get("https://abc7ny.com/place/elmhurst/")
soup5 = BeautifulSoup(url5.content, "html.parser")
headline = soup5.find("div", {"class": "headline"})
headline_text = soup5.find("div", {"class": "callout"})
headline = headline.get_text()
headline_text = headline_text.get_text()

day_url = requests.get("https://www.timeanddate.com/")
day_object = BeautifulSoup(day_url.content, "html.parser")
day = day_object.find("span", {"id":"ij1"})
date_today = day_object.find("span", {"id":"ij2"})
date_today_text = date_today.get_text()
day = day.get_text()


#youtube api
api_key = os.getenv("youtube_api")
youtube = build("youtube", "v3", developerKey = api_key)
pewdiepie = youtube.channels().list(part= "statistics", forUsername = "PewDiePie")
david_dobrik = youtube.channels().list(part= "statistics", id = "UCmh5gdwCx6lN7gEC20leNVA")
youtube_data2 = david_dobrik.execute()
david_dobrik_subcount = youtube_data2['items'][0]['statistics']['subscriberCount']
youtube_data = pewdiepie.execute()
pewdiepie_subcount = youtube_data['items'][0]['statistics']['subscriberCount']

#BTHS Info
url4 = requests.get("https://bths.edu")
soup4 = BeautifulSoup(url4.content, "html.parser")
content4 = soup4.find("div", {"role": "group"})
bths_today = content4.get_text()
bths_news = soup4.find("td", {"id": "r"})
bths_news = bths_news.get_text()
bths_news = " ".join(bths_news.split())
bths_today =" ".join(bths_today.split())


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
#quote 
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]["q"] + " -" + json_data[0]["a"]
  return quote

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
  channel = client.get_channel(real_channel_id)
  
  
  
  if message.author == client.user:
    return  

  #Old code example
  if message.content.startswith("$test"):
    await message.channel.send("Old code works when changed version ")



  #----------------------------
  if message.content == "$news":
    await channel.send("https://www.nydailynews.com"+ "\n" + headline2 + "\n"+ headline2_description + "\n \n" + headline3 + "\n \n"+ headline4 + "\n \n" + headline+ "\n \n" + headline_text)
  
  if message.content == "$david dobrik":
    await channel.send("David Dobrik currently has " + david_dobrik_subcount + " subscribers")
  if message.content.startswith("$pewdiepie"):
    await channel.send("PewDiePie currently has " + pewdiepie_subcount + " subscribers")
    
  if message.content == "$today":
    await channel.send("Day: "+ day + "\n Date " + date_today_text + "\n Period 1: 8:32-9:47 \n Period 2: 9:55 - 11:10 \n Period 3: 11:18- 12:33 \n Period 4: 12:41-1:56")
    await channel.send("Important news: " + bths_news)
    if "EVEN" in bths_today:
      await channel.send("Today is " + bths_today + " You have: Geometry, Free Period, Physics then DDP")
    else:
      await channel.send("Today is " + bths_today + " You have: Ela, Spanish, Free Period then World History")
  if message.content.startswith("$google"):
    await channel.send("Current price of google is " + "$" + google)
  if message.content.startswith("$apple"):
    await channel.send("Current price of apple stock is " + "$" + apple)

  if message.content.startswith("$help"):
    await channel.send("Commands: $inspire, $hello, $tesla, $apple, $google, $pewdiepie, $david dobrik, $today, $news, $random, $everyone")

  
  if message.content.startswith("$tesla"):
    await channel.send("Current price of tesla stock is: " + "$" + tesla)

    
  if message.content.startswith("$inspire"):
    quote = get_quote()
    await channel.send(quote)

  if message.content.startswith("help"):
    await channel.send("works")

    
keep_alive()
client.run(os.getenv("Token"))


