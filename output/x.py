import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import youtube_dl
import asyncio

# Ersetze 'YOUR_BOT_TOKEN' durch den tatsächlichen Token deines Bots
bot_token = 'MTE3MTkwODMyNDgzMzM3ODM2NQ.GHe-Hj.YFgKJ-vTBeh0AbSzuLh1RYxl4-9pmfnHoXtyJ8'

# Ersetze 'x.mp3' durch den Pfad zu deiner Audiodatei
audio_file_path = 'C:/Users/sar/Download/Y.mp3'

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is connected as {bot.user.name}')

    # Gehe durch alle Server, zu denen der Bot gehört
    for guild in bot.guilds:
        # Finde alle Voice-Channels auf dem Server
        for channel in guild.voice_channels:
            # Betrete den Voice-Channel
            await play_audio_in_channel(channel)

async def play_audio_in_channel(channel):
    try:
        # Betrete den Voice-Channel
        voice_channel = await channel.connect()

        # Spiele die Audiodatei ab
        voice_channel.play(discord.FFmpegPCMAudio(audio_file_path), after=lambda e: print('done', e))

        # Warte, bis die Audiodatei abgespielt wurde
        while voice_channel.is_playing():
            await asyncio.sleep(1)

        # Trenne die Verbindung zum Voice-Channel
        await voice_channel.disconnect()

    except Exception as e:
        print(f"Fehler beim Abspielen in {channel.name}: {e}")


# Starte den Bot
bot.run(bot_token)