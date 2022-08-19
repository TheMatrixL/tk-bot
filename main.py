import os
from discord.ext import commands
from tk import find_tk
from keep_alive import keep_alive
import url_data as ud

key = os.environ['key']

bot = commands.Bot(command_prefix='$', description="This is a TK Bot")

@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def tk(ctx, arg):
  
    async def send_message(category_url, brand, total_page):    
      data = find_tk(category_url)
      pages = 0
      for i in range(len(data)):
        if data[i]["Brand"] == brand:
          pages += 1
          await ctx.send(data[i]["Image"])
          await ctx.send("Price: " + data[i]["Price"])
          await ctx.send(data[i]["Url"])
      await ctx.send(f"{total_page}: {(pages)}")    
      
    if arg in ud.brand_name:
      await send_message(ud.today_arrivals, ud.brand_name[arg], "Today_arrivals")
      await send_message(ud.global_label, ud.brand_name[arg], "Global_label")
      await send_message(ud.clearance, ud.brand_name[arg], "Clearance")
      
    else:  
      await ctx.send("Please enter other brand.")
                     
keep_alive()
bot.run(key)






