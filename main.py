from keep_alive import keep_alive
import discord
import random
import os
from discord.ext import commands
from discord import DMChannel


client = commands.Bot(command_prefix = ".") 

with open('helpcommand.txt', 'r') as f:
  f_contents = f.read()
message = (f_contents)
link = "https://discord.gift/"
payam = 'Your Unlocked Nitro Code=>'
embed=discord.Embed(title="Nitro Code Is Ready", url="https://discord.gg/xgcZNSjanP", description="**Linke Shoma Be DM Ferestade Shod Lotfan Check Konid**", color=discord.Color.blue() )

@client.command()
async def gen(ctx):
    user = await client.fetch_user(f"{ctx.author.id}")
    chars = ['a', 'b', 'c', 'd',  'e','f', 'g', 'h','i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
  '1','2','3','4','5','6','7','8','9','0'
  ]
    gen = "".join(random.choices(chars, k=16))
    await ctx.send(embed = embed)
    await DMChannel.send(user,f"{link + gen}")    


keep_alive()       
# client = MyClient()
client.run(os.getenv('TOKEN'))
