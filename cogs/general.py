import discord
from discord.ext import commands

class General(commands.Cog):
    """Generic commands that don't belong in a particular category."""
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(General(bot))
