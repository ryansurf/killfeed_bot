from nitrado import NitradoAPI
import requests
import json
import re
import os


def player_count(NITRADO_TOKEN, URL):
    p = requests.get(URL, headers={'Authorization' : f'Bearer {NITRADO_TOKEN}', 'Accept': 'application/octet-stream'})

    parsed = json.loads(p.content)

    # retrives link for log download
    log_link = parsed['data']['token']['url']

    logs = requests.get(log_link)

    # this returns our logs
    logs_string = logs.content.decode()

    #splits log by each line
    log_lines = re.split('\n', logs_string)

    players = list()
    count = ''
    for line in log_lines:
        if "PlayerList log:" in line:
            count = (line.split("log: ",1)[1])
            players = list()
        player = re.search('"([^"]*)"|$', line).group()
        players.append(str(player))
    
    player_str = ''
    # add all players to players list 
    players = list(set(players))
    for p in range(len(players)):
        if players[p] =='':
            continue
        player_str += players[p] + " "
    # edge case if no players online 
    if len(player_str) == 0:
        return "No players online."
    # remove parenthesis at end of string 

    count = count + "\n"  + player_str 
    return count
