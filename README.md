# killfeed_bot

## Description
This app creates a Discord killfeed bot for the game DayZ for Ps4(although I think other platforms will work too, you have to change the end of the URL variable accordingly). The code parses through the server's logs on Nitrado(server hosting service) and when a PvP kill is detected,
it sends a message of the kill to a discord guild channel. It also has a command that returns the amount of players currently on the server, along with their
gamertags(called by "!players").

## How to install and run

Download all the files and keep them in the same directory.
You must obtain the following information to be stored in the .env file:
  - **DISCORD_TOKEN**: How your bot will obtain access to your discord guild
  - **CHANNEL**: The channel in your guild you would like your killfeed messages to output to
  - **PING_CHANNEL**: Channel where the ping(!players) commands will be outputted to
  - **NITRADO_TOKEN**: Token of your Nitrado server so you can obtain access to your logs
  - **URL**: URL of you Nitrado server's log(s) you want. Will look like: https://api.nitrado.net/services/{NITRADO_ID}/gameservers/file_server/download?file=/games/{SERVER_ID/noftp/dayzps/config/DayZServer_PS4_x64.ADM You must obtain your Nitrado ID and Server ID.
  - **TIME_WAIT**: How much time between the kill and message sent to the discord(in minutes)

Once you have done this, run main.py. A hosting service(https://www.writebots.com/discord-bot-hosting/) can be used, or the bot can be ran on a any machine that you are willing to keep running as long as you want your bot up(I run mine on a Raspberry Pi that is online 24/7, and push the code
out the terminal with screen(https://linuxize.com/post/how-to-use-linux-screen/).

## How to use

Once you invite the bot to your discord(s), you're ready to go!

Calling the bot with **!players** will output something like:

![alt text](https://user-images.githubusercontent.com/94500732/201502380-48efef7d-97b0-49cf-bbe0-075580840898.png)

When a PvP kill happens, the bot will output:
![alt text](https://user-images.githubusercontent.com/94500732/201502453-bdac1533-a7fb-4d3f-ab4c-31b220d7fd83.png)




