import discord
from discord.ext import commands, tasks
import asyncio

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

# Die Pfadangabe zur MP3-Datei, die im Loop abgespielt werden soll
mp3_file_path = 'DEIN_PFAD_ZUR_MP3_DATEI_HIER_EINFÜGEN'

@bot.event
async def on_ready():
    print(f'Bot is ready! Logged in as {bot.user.name}')
    play_mp3.start()

@tasks.loop(seconds=1)
async def play_mp3():
    for guild in bot.guilds:
        for voice_channel in guild.voice_channels:
            voice_channel = await voice_channel.connect()

            # Spiele die MP3-Datei im Loop ab
            voice_channel.play(discord.FFmpegPCMAudio(mp3_file_path), after=lambda e: print('done', e))
            while voice_channel.is_playing():
                await asyncio.sleep(1)

# Füge deinen Bot-Token hier ein
bot.run('MTE3MTkwODMyNDgzMzM3ODM2NQ.GHe-Hj.YFgKJ-vTBeh0AbSzuLh1RYxl4-9pmfnHoXtyJ8')
