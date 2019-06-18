import sys
import discord
from discord.ext import commands

class Admin(commands.Cog):
    """Administrative commands for managing the server."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="purge", hidden=True)
    @commands.has_role("Admin")
    async def purge(self, ctx, *, messages: int=100):
        """Purges up to 100 messages per command execution. Administrative use only."""
        count = await ctx.channel.purge(limit=messages)
        message = await ctx.send(f"Purged {len(count)} messages.")
        await message.delete(delay=5)

    @commands.command(name="purgechannel", hidden=True)
    @commands.has_role("Admin")
    async def purgechannel(self, ctx):
        """Completely purges a text channel by cloning it and deleting the old one. Administrative use only."""
        newchannel = await ctx.channel.clone(name=ctx.channel.name, reason=sys._getframe().f_code.co_name)
        oldchannel = await ctx.channel.delete(reason=sys._getframe().f_code.co_name)
        message = await newchannel.send("Channel purged. Don't forget to move this channel back to where it belongs, Guardian.")
        await message.delete(delay=10)

def setup(bot):
    bot.add_cog(Admin(bot))
