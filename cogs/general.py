import arrow
import discord
from discord.ext import commands

class General(commands.Cog):
    """Generic commands that don't belong in a particular category."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="timezone", hidden=False)
    async def timezone(self, ctx, *, name: str="utc"):
        """Returns the current time in a specified timezone. If a time is specified, it will return the specified time in that timezone instead."""
        await ctx.send("This command is not set up properly yet.")

def setup(bot):
    bot.add_cog(General(bot))
