from keep_alive import keep_alive
import discord
import random
import os
from discord.ext import commands
from discord import DMChannel


client = commands.Bot(command_prefix = "place-prefix") 

link = "https://discord.gift/"
payam = 'Your Unlocked Nitro Code=>'

embed=discord.Embed(title="Nitro Code Is Ready", url="https://discord.gg/vgnhGXabNw", description="Salam Baradar Man Baraie Shoma Link Nitro Gift Ro Estekhraj Kardam 🙂 , Lotfan Dm Khodra Check Konid Ta Linke Khodra Bebinid 🙂 Baraye Estefade Mojaddad Az Bot Commande Ro Be Ro Bezanid **.gen**", color=discord.Color.blue())
embed.set_footer(text="Created By Mr.SIN RE#1528")

@client.command()
async def gen(ctx):
  if ctx.message.channel.id == (place-channel-id) or ctx.message.channel.id == (place-channel-id): #if you have some channel paste this code <or ctx.message.channel.id == (place-channel-id)> and enjoy 🙂
    user = await client.fetch_user(f"{ctx.author.id}")
    chars = ['a', 'b', 'c', 'd',  'e','f', 'g', 'h','i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
  '1','2','3','4','5','6','7','8','9','0'
  ]
    gen = "".join(random.choices(chars, k=16))
    await ctx.send(embed = embed)
    await DMChannel.send(user,f"{payam + link + gen}")       


keep_alive()       
client.run(os.getenv('TOKEN'))
