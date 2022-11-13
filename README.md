# killfeed_bot

## Description
This app creates a Discord killfeed bot for the game DayZ. The code parses through the server's logs on Nitrado(server hosting service) and when a kill is detected,
it sends a message of the kill to a discord guild channel. It also has a command that returns the amount of players currently on the server, along with their
gamertags(called by "!players").

## How to install and run

Download all the files and keep them in the same directory.
You must obtain the following information to be stored in the .env file:
  - **DISCORD_TOKEN**: How your bot will obtain access to your discord guild
  - **CHANNEL**: The channel in your guild you would like your killfeed messages to output to
  - **PING_CHANNEL**: Channel where the ping(!players) commands will be outputted to
  - **NITRADO_TOKEN**: Token of your Nitrado server so you can obtain access to your logs
  - **URL**: URL of you Nitrado server's log(s) you want
  - **TIME_WAIT**: How much time between the kill and message sent to the discord(in minutes)
