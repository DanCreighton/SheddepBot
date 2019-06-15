import json
import discord
from discord.ext import commands

description = '''Sheddep Bot is a Discord bot built upon the Pydest API wrapper for Destiny 2. It's main purpose is to assist in the management of the Sheddep clan community and provide a more on-demand way to deliver in-game information to its members.'''

# Specify the extensions (cogs) to load when the bot starts up
startup_extensions = ["cogs.admin"]

bot = commands.Bot(command_prefix="/", description=description)

# Run this code when an error occurs
@bot.event
async def on_command_error(ctx, error):
    err = type(error).__name__
    msg = error
    # Message Dan about the error
    await bot.get_user(226030198095740929).send(f"Error in **{ctx.guild.name}** #{ctx.channel.name} ({err})\n\n{msg}\n\nOriginal message:\n{ctx.message.author} — *\"{ctx.message.content}\"*")
    # Notify the user about it
    await ctx.send("Apologies, Guardian, there was an error with your request. A report has been sent to the developers.")

# Run this code when the bot is ready
@bot.event
async def on_ready():
    ### https://discordpy.readthedocs.io/en/latest/api.html#discord.on_ready ###
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id}) successfully\nDiscord.py version {discord.__version__}\n')
    # Change bot presence
    await bot.change_presence(activity=discord.Activity(type=2, name="commands"))
    print(f'Changed presence to \"Listening to commands\"')

# Load cogs
if __name__ == '__main__':
    for extension in startup_extensions:
        bot.load_extension(extension)

# Read credentials.json
with open("credentials.json", "r") as file:
    credentials = json.load(file)
token = credentials["token"]

# Run bot
bot.run(token, bot=True, reconnect=True)
