import arrow
import json
import discord
from discord.ext import commands

class General(commands.Cog):
    """Generic commands that don't belong in a particular category."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="timezone", hidden=False)
    async def timezone(self, ctx, *, abbr: str=None, tztime: str=None):
        """Returns the current time in a specified timezone. If a time is specified, it will return the specified time in that timezone instead."""
        # Open JSON file containing timezone data
        with open("timezones.json") as file:
            tzdata = json.load(file)
            print(f"Loaded JSON data from file \"{file.name}\"")
        # Get the current UTC time
        now = arrow.utcnow()
        # Check if the user provided the abbr (timezone abbreviation) parameter
        if abbr != None:
            # If a time wasn't provided
            if tztime == None:
                # Initialise the appropriate lists
                names = []
                times = []
                # Iterate through the timezone data
                for timezone in tzdata:
                    # If the provided abbr parameter exists in the timezone data
                    if abbr.upper() == timezone['abbr']:
                        # Add the timezone name to a list
                        names.append(timezone['value'])
                        # Shift the UTC time by the corresponding offset
                        times.append(now.shift(hours=timezone['offset']))
                # Check if there are multiple timezones found
                if len(times) > 1:
                    # Construct the message
                    msg = f"There are several times listed under **{abbr.upper()}**:"
                    for t in range(len(times)):
                        msg += f"\nThe current time in **{names[t]}** is {times[t].format('h:mma')}."
                    # Send message to channel
                    await ctx.send(msg)
                # Otherwise
                else:
                    # Send message to channel
                    await ctx.send(f"The current time in **{names[0]}** is {times[0].format('h:mma')}.")
        # If the timezone abbreviation wasn't provided
        else:
            # Send message to channel
            await ctx.send("Please specify a timezone, Guardian.")

def setup(bot):
    bot.add_cog(General(bot))
