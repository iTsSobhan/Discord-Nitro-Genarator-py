from keep_alive import keep_alive
import discord
import random
import os
import random
import os
from discord.ext import commands

with open('helpcommand.txt', 'r') as f:
    f_contents = f.read()
message = (f_contents)
def gen():
    chars = ['a', 'b', 'c', 'd',  'e','f', 'g', 'h','i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    '1','2','3','4','5','6','7','8','9','0'
    ]
    return "".join(random.choices(chars, k=16))

link = "https://discord.gift/"
payam = 'Your Unlocked Nitro Code=>'
embed=discord.Embed(title="Nitro Code Is Ready", url="https://discord.gg/xgcZNSjanP", description="**Linke Shoma Be DM Ferestade Shod Lotfan Check Konid**", footer='Created by Sobhan.SRZA#2153', color=discord.Color.blue() )

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        if message.content == '.gen':
          await message.channel.send(embed=embed)
          await message.author.send(payam + link + gen())

keep_alive()       
client = MyClient()
client.run(os.getenv('TOKEN'))
