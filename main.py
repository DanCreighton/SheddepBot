import discord
from discord.ext import commands

description = '''a Discord bot built upon the Pydest API wrapper for Destiny 2. It's main purpose is to assist in the management of the Sheddep clan community and provide a more on-demand way to deliver in-game information to its members.'''

# Specify the extensions (cogs) to load when the bot starts up
startup_extensions = ["cogs.admin"]

bot = commands.Bot(command_prefix="¬", description=description)

@bot.event
async def on_ready():
    ### https://discordpy.readthedocs.io/en/latest/api.html#discord.on_ready ###
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id}) successfully\nDiscord.py version {discord.__version__}\n')
    # Changes bot presence
    await bot.change_presence(activity=discord.Activity(type=2, name="commands"))
    print(f'Changed presence to \"Listening to commands\"')

if __name__ == '__main__':
    for extension in startup_extensions:
        bot.load_extension(extension)

bot.run('NTc0MjI1MDAwNDU0Njg0Njcy.XQQg9g.80vEzLMm4DYnALDbTFeHYiMSRug', bot=True, reconnect=True)
