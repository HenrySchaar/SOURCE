import discord
from discord.ext import commands

# Ersetze 'YOUR_BOT_TOKEN' durch den tatsächlichen Token deines Bots
bot_token = 'Bot token'

# Erstelle eine Variable für die benötigten Intents
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

# Eine Datenstruktur, um Warnungen zu speichern: {guild_id: {user_id: [warnings]}}
warnings_dict = {}

@bot.event
async def on_ready():
    print(f'Bot is connected as {bot.user.name}')

@bot.command(name='warn', pass_context=True)
async def warn(ctx, member: discord.Member, *, reason):
    # Sende Warnung per DM
    try:
        await member.send(f"You have been warned in {ctx.guild.name} for the following reason: {reason}")
    except discord.Forbidden:
        await ctx.send(f"Failed to send DM to {member.mention}. They may have DMs disabled.")
    
    # Speichere die Warnung in der Liste
    guild_id = ctx.guild.id
    user_id = member.id

    if guild_id not in warnings_dict:
        warnings_dict[guild_id] = {}

    if user_id not in warnings_dict[guild_id]:
        warnings_dict[guild_id][user_id] = []

    warnings_dict[guild_id][user_id].append(reason)
    await ctx.send(f"{member.mention} has been warned for: {reason}")

@bot.command(name='warnings', pass_context=True)
async def get_warnings(ctx, member: discord.Member):
    # Zeige alle Warnungen des Benutzers auf dem aktuellen Server an
    guild_id = ctx.guild.id
    user_id = member.id

    if guild_id in warnings_dict and user_id in warnings_dict[guild_id]:
        warnings = warnings_dict[guild_id][user_id]
        await ctx.send(f"{member.mention} has the following warnings on this server:\n" + '\n'.join(warnings))
    else:
        await ctx.send(f"{member.mention} has no warnings on this server.")
# Erstelle eine Variable für die benötigten Intents
# Ersetze 'reports_channel_id' durch die tatsächliche ID des "reports"-Kanals
reports_channel_id = 123456789012345678

# Erstelle eine Variable für die benötigten Intents
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is connected as {bot.user.name}')

@bot.command(name='report', pass_context=True)
async def report(ctx, member: discord.Member, *, reason):
    # Finde den "reports"-Kanal
    reports_channel = ctx.guild.get_channel(1183506551869292594)

    if reports_channel is None:
        return await ctx.send("Der 'reports'-Kanal wurde nicht gefunden. Bitte überprüfe die Einstellungen.")

    # Sende den Report in den "reports"-Kanal
    report_embed = discord.Embed(
        title="New Report",
        description=f"**Reporter:** {ctx.author.mention}\n**Reported User:** {member.mention}\n**Reason:** {reason}",
        color=discord.Color.orange()
    )
    await reports_channel.send(embed=report_embed)

    await ctx.send("Report sent.")
# Erstelle eine Variable für die benötigten Intents
# Erstelle eine Variable für die benötigten Intents
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is connected as {bot.user.name}')

@bot.event
async def on_message(message):
    # Überprüfe, ob :joy: in der Nachricht enthalten ist
    if ":joy:" in message.content:
        # Reagiere auf die Nachricht mit einem Emoji (kann angepasst werden)
        await message.add_reaction('😄')

        # Gib die Nachricht in der Konsole aus
        print(f"Reagiert auf Nachricht: '{message.content}' von {message.author.name}")

    # Damit andere Events weiterhin verarbeitet werden
    await bot.process_commands(message)

# Starte den Bot
bot.run(bot_token)
