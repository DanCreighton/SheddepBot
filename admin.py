import discord
from discord.ext import commands

class Admin(commands.Cog):
    """Administrative commands for managing the server."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="purge", aliases=["clear", "wipe"], hidden=True)
    @commands.has_role("Admin")
    async def purge(self, ctx):
        """Purges a text channel of all messages."""
        await ctx.send("Purges a text channel of all messages. Administrative command only. (This command isn't set up properly yet.)")

def setup(bot):
    bot.add_cog(Admin(bot))
