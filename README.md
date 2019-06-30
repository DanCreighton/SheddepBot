# Sheddep Bot
***Sheddep Bot is a Discord bot built upon the Pydest API wrapper for Destiny 2. It's main purpose is to assist in the management of the Sheddep clan community and provide a more on-demand way to deliver in-game information to its members.***

If you want to run this bot yourself, you'll need to begin by creating a `credentials.json` file in the root directory of the project. This file should contain two things: the Bungie API key and the Discord bot token. The former is required for Pydest to work correctly, and the latter is required for the bot to connect to Discord's servers.
```
{
  "api-key": "bungie_api_key_here",
  "token": "discord_bot_token_here"
}
```
Additionally, you should install the prerequisite [dependencies](#dependencies) via PyPI on the host system before attempting to run Sheddep Bot. You'll also need to create a bot user at the [Discord developer portal](https://discordapp.com/developers/applications/) and invite it to your server with the following permissions:

* Manage Channels
* Manage Messages
* Read Message History

These permissions are associated with the functionality of certain commands, as outlined in the [Commands](#commands) section.

## Dependencies
This project relies on several dependencies to function correctly. Run the following commands in the command line to install or update them.
* discord.py (v1.2.3)
  * `python -m pip install -U discord.py`
  * Provides Discord bot functionality.
* Arrow (v0.14.2)
  * `python -m pip install -U arrow`
  * Used for the bot's time calculations.
* Pydest (v0.1.0)
  * `python -m pip install -U git+https://github.com/jgayfer/pydest`
  * Used to retrieve data from the Destiny 2 API.

## Commands
### Implemented
|Usage|Brief description|Associated permissions|
|:---|:---|:---|
|`help <command>`|Displays a message with details about a command, or lists all commands if not specified.|
|`purge <count>`|Purges up to 100 messages per command execution. Administrative use only.|Manage Messages, Read Message History|
|`purgechannel`|Completely purges a text channel by cloning it and deleting the old one. Administrative use only.|Manage Messages, Manage Channels|
### In Progress
|Usage|Brief description|
|:---|:---|
|`timezone <name> [time]`|Returns the current time in a specified timezone. Optionally, if a time is specified, it will convert the specified time instead of the current time.|
|`banword <word>`|Bans a specific word from being sent in messages. Administrative use only.|
|`unbanword <word>`|Unbans a word that was previously banned with the `banword` command. Administrative use only.|
|`unbanallwords`|Unbans all words that were previously banned with the `banword` command. Administrative use only.|
|`bannedwords`|Shows a list of words currently banned with the `banword` command.|
|`autopurgechannel <#channel> <duration>`|Marks a channel to have messages be automatically purged when they've existed for a specified amount of time. Administrative use only.|
### Planned
* `lore`
  * For lore-related commands, including managing weekly lore discussions and displaying lore book details.
* `tournament`
  * For setting up and managing Gambit and Crucible tournaments.
---
This project is developed and maintained by [@dancreightondev](https://twitter.com/dancreightondev).
