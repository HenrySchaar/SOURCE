import discord
from discord.ext import commands
import os
token = "MTE4NDU1Nzk1NzA5OTMwNzEwMQ.GTrV0U.m4Hmg7D2q_vEn3Vxq48ndR7HRHXhI8OozHMJ5Q"

intents = discord.Intents.default()
intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is ready! Logged in as {bot.user.name} - {bot.user.id}')

@bot.command(name="calculate")
async def calculate(ctx, *, expression):
    try:
        result = eval(expression)
        await ctx.send(f'The Result is: {result}')
    except Exception as e:
        await ctx.send(f'An error occurred: {str(e)}')

# Setzen Sie Ihren Bot-Token hier ein
bot.run(token)
