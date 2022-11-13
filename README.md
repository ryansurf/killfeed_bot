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

## How to use

Once you invite the bot to your discord(s), you're ready to go!

Calling the bot with !players will output something like:

https://github.com/ryansurf/killfeed_bot/blob/master/images/Screen%20Shot%202022-11-12%20at%206.08.36%20PM.png?raw=true![image](https://user-images.githubusercontent.com/94500732/201502380-48efef7d-97b0-49cf-bbe0-075580840898.png)

