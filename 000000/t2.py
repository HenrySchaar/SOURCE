import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

# Füge die ID des Ziel-Channels hier ein
target_channel_id = 1183497201947775016

@bot.event
async def on_ready():
    print(f'Bot is ready! Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    # Verhindere, dass der Bot auf seine eigenen Nachrichten reagiert
    if message.author == bot.user:
        return

    # Verhindere, dass der Bot auf Nachrichten reagiert, die nicht im Ziel-Textkanal gesendet wurden
    if message.channel.id != target_channel_id:
        return

    # Zeige die empfangene Nachricht im Terminal an
    print(f'**Nickname:** {message.author.display_name}\n**Username:** {message.author.name}#{message.author.discriminator}\n**Nachricht:** {message.content}')

    # Lasse den Bot die Nachrichten weiterhin normal verarbeiten
    await bot.process_commands(message)

# Füge deinen Bot-Token hier ein
bot.run('MTE3MTkwODMyNDgzMzM3ODM2NQ.GHe-Hj.YFgKJ-vTBeh0AbSzuLh1RYxl4-9pmfnHoXtyJ8')
