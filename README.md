# Emma - a bot for Fire Emblem Cipher
Note: this bot is an old project from before Cipher stopped releasing sets that may not work anymore due to updates to the Discord API (pre-intents)

Emma is a helper bot for the Fire Emblem Cipher card game.

## Commands
The bot accepts card names in the following formats:
* Full card name - **Lucina, Heiress to the Exalt's Blood**
* Character name only - **Lucina**
* Character name and cost - **Lucina 1** or **Lucina 4(3)**
* Character name and set - **Lucina B01** for Lucina from Booster Set 1

If there are multiple results for the query, the bot displays options which can be chosen between

`fe0?card <card name>` - shows card text for the specified card  
`fe0?image <card name>` - shows the (untranslated) card image - fetched from https://fecipher.jp/ which has been taken down due to the end of the game in October 2020.
