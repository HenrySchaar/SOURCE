import discord
from discord.ext import commands

# Ersetze 'YOUR_BOT_TOKEN' durch den tatsächlichen Token deines Bots
bot_token = 'MTE3MTkwODMyNDgzMzM3ODM2NQ.GHe-Hj.YFgKJ-vTBeh0AbSzuLh1RYxl4-9pmfnHoXtyJ8'

# Erstelle eine Variable für die benötigten Intents
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is connected as {bot.user.name}')

@bot.command(name='dc', pass_context=True)
@commands.has_permissions(administrator=True)  # Benötigt Administratorberechtigungen
async def delete_channel(ctx):
    channel = ctx.message.channel

    try:
        # Lösche den Kanal
        await channel.delete()
        print(f"Channel '{channel.name}' in {ctx.guild.name} deleted.")
    except Exception as e:
        print(f"Error deleting channel '{channel.name}' in {ctx.guild.name}: {e}")
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is connected as {bot.user.name}')

@bot.command(name='say', pass_context=True)
async def say(ctx, *, message):
    # Sende die Nachricht und lösche sie nach 5 Sekunden (kann angepasst werden)
    await ctx.send(message, delete_after=5)

    # Lösche die ursprüngliche Befehlsnachricht des Benutzers
    await ctx.message.delete()
# Starte den Bot
bot.run(bot_token)
