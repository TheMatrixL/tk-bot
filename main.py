import os
import discord
import brand as bd
from tk import find_tk
from keep_alive import keep_alive

key = os.environ['key']

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    async def send_message(category, brand):
      data = find_tk(category)
      pages = 0
      for i in range(len(data)):
        if data[i]["Brand"] == brand:
          pages += 1
          await message.channel.send(data[i]["Image"])
          await message.channel.send("Price: " + data[i]["Price"])
          await message.channel.send(data[i]["Url"])
      await message.channel.send("Today_arrivals Total: " + str(pages))
      
    if message.author == client.user:
        return

    if message.content.startswith("$mk"):
      await send_message(bd.today_arrivals, bd.brand_name["$mk"])
      await send_message(bd.global_label, bd.brand_name["$mk"])
          
    elif message.content.startswith("$ck"):
      await send_message(bd.today_arrivals, bd.brand_name["$ck"])
      await send_message(bd.global_label, bd.brand_name["$ck"])
    
keep_alive()
client.run(key)






