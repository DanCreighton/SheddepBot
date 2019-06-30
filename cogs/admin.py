import sys
import discord
from discord.ext import commands

class Admin(commands.Cog):
    """Administrative commands that help to manage the server."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="purge", hidden=True)
    @commands.has_role("Admin")
    async def purge(self, ctx, *, messages: int=100):
        """Purges up to 100 messages per command execution. Administrative use only."""
        count = await ctx.channel.purge(limit=messages+1)
        message = await ctx.send(f"Purged {len(count)-1} messages.")
        await message.delete(delay=5)

    @commands.command(name="purgechannel", aliases=["pc"], hidden=True)
    @commands.has_role("Admin")
    async def purgechannel(self, ctx):
        """Completely purges a text channel by cloning it and deleting the old one. Administrative use only."""
        newchannel = await ctx.channel.clone(name=ctx.channel.name, reason=sys._getframe().f_code.co_name)
        oldchannel = await ctx.channel.delete(reason=sys._getframe().f_code.co_name)
        message = await newchannel.send("Channel purged. Don't forget to move this channel back to where it belongs, Guardian.")
        await message.delete(delay=10)

    @commands.command(name="autopurgechannel", aliases=["autopc"], enabled=False, hidden=True)
    @commands.has_role("Admin")
    async def autopurgechannel(self, ctx):
        """Marks a channel to have messages be automatically purged when they've existed for a specified amount of time. Administrative use only."""
        await ctx.send("This command is incomplete.")

    @commands.command(name="banword", aliases=["bw"], enabled=False, hidden=True)
    @commands.has_role("Admin")
    async def banword(self, ctx):
        """Bans a specific word from being sent in messages. Administrative use only."""
        await ctx.send("This command is incomplete.")

    @commands.command(name="unbanword", aliases=["ubw"], enabled=False, hidden=True)
    @commands.has_role("Admin")
    async def unbanword(self, ctx):
        """Unbans a word that was previously banned with the banword command. Administrative use only."""
        await ctx.send("This command is incomplete.")

    @commands.command(name="unbanallwords", aliases=["uba"], enabled=False, hidden=True)
    @commands.has_role("Admin")
    async def unbanallwords(self, ctx):
        """Unbans all words previously banned with the `banword` command. Administrative use only."""
        await ctx.send("This command is incomplete.")

    @commands.command(name="bannedwords", aliases=["bwl", "bwlist"], enabled=False, hidden=False)
    async def bannedwords(self, ctx):
        """Shows a list of words banned with the `banword` command."""
        await ctx.send("This command is incomplete.")

def setup(bot):
    bot.add_cog(Admin(bot))
