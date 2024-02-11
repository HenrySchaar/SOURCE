import discord
from discord.ext import commands
import datetime

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

# Speichere Warnungen in einem Dictionary
warnings = {}

@bot.event
async def on_ready():
    print(f'Bot is ready! Logged in as {bot.user.name}')

@bot.command(name='warn')
async def warn(ctx, user: discord.User, *, reason: str):
    # Überprüfe, ob der Benutzer bereits Warnungen hat
    if user.id not in warnings:
        warnings[user.id] = []

    # Füge die Warnung hinzu
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    warning_info = {'reason': reason, 'time': current_time}
    warnings[user.id].append(warning_info)

    await ctx.send(f'created warning for {user.mention}. reason: {reason}')

@bot.command(name='warnings')
async def get_warnings(ctx, user: discord.User):
    # Überprüfe, ob der Benutzer Warnungen hat
    if user.id not in warnings or not warnings[user.id]:
        await ctx.send(f'{user.mention} has no warnings.')
        return

    # Sende alle Warnungen des Benutzers
    for idx, warning_info in enumerate(warnings[user.id], 1):
        reason = warning_info['reason']
        time = warning_info['time']
        await ctx.send(f'**Warning {idx}**: reason: {reason}, time: {time}')

# Füge deinen Bot-Token hier ein
bot.run('MTE3MTkwODMyNDgzMzM3ODM2NQ.GHe-Hj.YFgKJ-vTBeh0AbSzuLh1RYxl4-9pmfnHoXtyJ8')
