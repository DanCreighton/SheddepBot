import discord
from discord.ext import commands

class Admin(commands.Cog):
    """Administrative commands for managing the server."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="purge", aliases=["clear", "wipe", "prune"], hidden=True)
    @commands.has_role("Admin")
    async def purge(self, ctx):
        """Purges a text channel of all messages, with the exception of pinned messages."""
        await ctx.message.channel.purge(limit=None, check=lambda msg: not msg.pinned, bulk=True)
        success = await ctx.send("Channel purged.")
        await ctx.

def setup(bot):
    bot.add_cog(Admin(bot))
