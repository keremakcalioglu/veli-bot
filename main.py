from datetime import date
import datetime
import discord
from discord.ext import commands
import random
from discord.ext.commands import has_permissions, MissingPermissions
client = commands.Bot(command_prefix ="/")
import calendar
from discord.utils import get



@client.event
async def on_message(message):

    if message.content == "sa" or message.content == "Sa" or message.content == "SA" or message.content ==   "sA":
        await message.channel.send("as yeğen")

    await client.process_commands(message)

@client.event
async def on_ready():
    print('Bot is ready')





@client.command()
@has_permissions(manage_messages=True)
async def purge(ctx, amount=5 ,):

    bruh = amount + 1
    await ctx.channel.purge(limit=bruh)



@client.command()
@has_permissions(manage_messages=True)
async def purgeall(ctx):
    messages = await ctx.channel.history().flatten()
    await ctx.channel.purge(limit=len(messages ) +1)

@client.command( brief="Karizma benim!", aliases=['k'])
async def karizma(ctx):

    message = ctx.message
    channel_id = ctx.message.author.voice.channel.id
    channel = client.get_channel(channel_id)


    await channel.connect()




    await ctx.send("Karizma Benim  - Veli Çıracı")
    print("Someone wants to play music let me get that ready for them...")
    voice = get(client.voice_clients, guild=ctx.guild)

    voice.play(discord.FFmpegPCMAudio("Karizma Benim (official video).mp3"))
    voice.volume = 100
    voice.is_playing()

@client.command()
@has_permissions(administrator=True)
async def msg(ctx,*,msg:str):
    await discord.Message.delete(ctx.message)
    await ctx.send(str(msg))

@client.command(brief="Botu ses kanalından çıkarır", aliases=['l', 'le', 'lea'])
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.disconnect()

    else:
        await ctx.send("Ses kanalında değilim yeğen")

@client.command(aliases = ["söz","s"])
async def soz(ctx):
    f = open("hebele.txt","r")
    f = f.readlines()

    soz = random.choice(f)
    await ctx.send(soz)

@client.command()
async def yardım(ctx):
    author =ctx.message.author

    embed=discord.Embed(
        colour = discord.Colour.orange()
    )

    embed.set_author(name ="YARDIM")
    embed.add_field(name="/karizma   ", value ="Veli Hoca'nın Karizma Benim şarkısını çalar" ,inline=False)
    embed.add_field(name="/leave ", value="Veli Hoca \'Karizma Benim\' şarkısını söyledikten sonra ses nalından ayrılmasını sağlar", inline=False)
    embed.add_field(name="/soz",value= "Veli Hoca karizmasına yaraşır bir özlü söz söyler ")
    embed.add_field(name="Diğer Özellikler: ",value="\"sa\" diyince size \"as yeğen\" diye cevap verir")

    await ctx.channel.send(author, embed=embed)

client.run("NzU4NzExNTc1NjY1ODM2MDYy.X2y7Nw.PEYCuT3Ddtf3dkFV58yPk-ItrUM")