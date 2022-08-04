import os
import discord
from keep_alive import keep_alive
from tk import find_tk, global_label, big_brand_drop, today_arrivals
key = os.environ['key']

brand_name = {
  "$mk": "Michael Kors", 
  "$ck": "Calvin Klein"
}

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    pages = 0
    if message.author == client.user:
        return

    if message.content.startswith("$mk"):
      data = find_tk(today_arrivals)
      for i in range(len(data)):
        if data[i]["Brand"] == brand_name["$mk"]:
          pages += 1
          await message.channel.send(data[i]["Image"])
          await message.channel.send("Price: " + data[i]["Price"])
          await message.channel.send(data[i]["Url"])
      await message.channel.send("Today_arrivals Total: " + str(pages))
      
      data = find_tk(global_label)
      for i in range(len(data)):
        if data[i]["Brand"] == brand_name["$mk"]:
          pages += 1
          await message.channel.send(data[i]["Image"])
          await message.channel.send("Price: " + data[i]["Price"])
          await message.channel.send(data[i]["Url"])
      await message.channel.send("Global_label Total: " + str(pages))
          
    elif message.content.startswith("$ck"):
      data = find_tk(today_arrivals)
      for i in range(len(data)):
        if data[i]["Brand"] == brand_name["$ck"]:
          pages += 1
          await message.channel.send(data[i]["Image"])
          await message.channel.send("Price: " + data[i]["Price"])
          await message.channel.send(data[i]["Url"])
      await message.channel.send("Today_arrivals Total: " + str(pages)) 

      data = find_tk(global_label)
      for i in range(len(data)):
        if data[i]["Brand"] == brand_name["$mk"]:
          pages += 1
          await message.channel.send(data[i]["Image"])
          await message.channel.send("Price: " + data[i]["Price"])
          await message.channel.send(data[i]["Url"])
      await message.channel.send("Global_label Total: " + str(pages))
    
keep_alive()
client.run(key)






