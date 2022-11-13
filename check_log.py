from nitrado import NitradoAPI
import requests
import json
import re
from datetime import datetime
import time


def kill_string(NITRADO_TOKEN, URL, TXT_FILE):
    p = requests.get(URL, headers={'Authorization' : f'Bearer {NITRADO_TOKEN}', 'Accept': 'application/octet-stream'})

    parsed = json.loads(p.content)

    # retrives link for log download
    log_link = parsed['data']['token']['url']

    logs = requests.get(log_link)

    # this returns our logs
    logs_string = logs.content.decode()

    #splits log by each line
    log_lines = re.split('\n', logs_string)


    #check each line for player killed by another player. Killed if "DEAD" and "by Player" or "killed by" in line(have to see actual kill in logs to make sure)
    for line in log_lines:
        # adjust to find both players
        #line = '19:12:05 | Player "g352dl428" (DEAD) (id=yFMx3zRIDvLDU4fg2WsfMhUwXF2JXqAxEGFauBcOphc= pos=<1768.7, 7208.1, 232.0>) killed by Player "AkaUnagomi_test" (id=mzCeNoLIUfgG8ul-tpllzw8kWlF2dXkNjUBtGTWTam4= pos=<1764.2, 7207.7, 232.2>) with SSG 82 from 4.53196 meters' 
        if line.count('"') >= 4 and "killed" in line:
            killed_txt = re.sub(r'\([^)]*\)', '', line)
            # if killed_txt in kills.txt file we continue(kill has already been documented, keep looking for more kills). Else if it is a new kill, we break
            if check_txt(killed_txt, TXT_FILE) == '':
                continue
            else:
                break
            #time = re.findall('\d\d:\d\d:\d\d', line)
        else:
            killed_txt = ''

    if len(killed_txt) > 1:
        
        # checks if kill already in txt file and returns empty string if True 
        if check_txt(killed_txt, TXT_FILE) == '':
            return ''
        add_txt(killed_txt, TXT_FILE)
        return killed_txt

    # if nobody killed we return an empty string 
    else:
        return ''

# adds most recent kill to our text file 
def add_txt(line, txtFile):
    with open(txtFile, "a") as f:
        f.write(line + '\n')

# returns nothing is kill is already in our txt file 
def check_txt(line, txtFile):
    with open(txtFile) as f:
        if line in f.read():
            return ''
    return line

# adds kill to txt file to wait twnety minutes
def add_twenty(line, waitTxt):
    with open(waitTxt, "a") as f:
        time = str(datetime.now())
        f.write(line + "||" + time + "\n")
    
# check if kill happened {TIME_WAIT} minutes ago 
def check_twenty(waitTxt, TIME_WAIT):
    with open(waitTxt, "r") as f:
        delete_lines = list()
        cur_time = datetime.now()
        for line in f:
            time_kill = line.split("||",1)[1].strip()
            line_time = datetime.strptime(time_kill, "%Y-%m-%d %H:%M:%S.%f")
            # check if time greater than 20 
            timedelta = cur_time - line_time
            minutes = timedelta.seconds / 60
            if minutes >= TIME_WAIT:
                delete_lines.append(line)
    return delete_lines
        

# deletes lines in txt file when minutes >= 20
def delete_lines(waitTxt, delete_lines):
    with open(waitTxt, "r") as f:
        lines = f.readlines()
    with open(waitTxt, "w") as f2:
        for line in lines:
           if line not in delete_lines:
                f2.write(line)
