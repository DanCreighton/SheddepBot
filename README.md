# Sheddep Bot
***Sheddep Bot is a Discord bot built upon the Pydest API wrapper for Destiny 2. It's main purpose is to assist in the management of the Sheddep clan community and provide a more on-demand way to deliver in-game information to its members.***

Before the bot can be run, you'll need to create a `credentials.json` file in the root directory of this project. This file should contain two things: the Bungie API key and the Discord bot token. The former is required for Pydest to work correctly, and the latter is required for the bot to connect to Discord's servers.

```
{
  "api-key": "bungie_api_key_here",
  "token": "discord_bot_token_here"
}
```

## Commands
#### Implemented
* `help <command>`
  * Displays a message with details about a command, or lists all commands if not specified.
#### In Progress
* `purge`, `clear`, `wipe`, `prune`
  * Purges a text channel of all messages. Administrative command only.
#### Planned
* `lore`
  * For lore-related commands, including managing weekly lore discussions and displaying lore book details.
---
This project is developed and maintained by [@dancreightondev](https://twitter.com/dancreightondev).
