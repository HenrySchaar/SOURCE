import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is ready! Logged in as {bot.user.name}')

@bot.command(name='kick')
async def kick_user(ctx, user_id: int):
    # Überprüfe, ob der Benutzer, der den Befehl ausführt, die Berechtigung zum Kicken hat
    if ctx.message.author.guild_permissions.kick_members:
        try:
            user = await bot.fetch_user(user_id)
            await ctx.guild.kick(user, reason="Kick durch Bot-Befehl")
            await ctx.send(f'Benutzer {user.name}#{user.discriminator} wurde gekickt.')
        except discord.NotFound:
            await ctx.send('Benutzer nicht gefunden.')
        except discord.Forbidden:
            await ctx.send('Ich habe nicht genug Berechtigungen, um diesen Benutzer zu kicken.')
    else:
        await ctx.send('Du hast nicht die Berechtigungen, um Benutzer zu kicken.')

# Füge deinen Bot-Token hier ein
bot.run(input("Bot token: "))
