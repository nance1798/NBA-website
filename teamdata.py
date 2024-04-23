import re
import requests
from bs4 import BeautifulSoup


req = requests.get("https://www.basketball-reference.com/leagues/NBA_2024_ratings.html")

soup = BeautifulSoup(req.content, "html.parser")
print('yes')

requests = soup.find(id="all_ratings")

theTeams = [] 
teamName = []
teamWins = []
teamLosses = []
teamOffense = []
teamDefense = []
teamRating = []
projectedWins = []


for team in requests.find_all('tr'):
    newTeam = team.text
    theTeams.append(newTeam)


for team in theTeams [2:]:   
    name = re.split('(\d+)',team)
    
    if(name[2] == 'Philadelphia '):
        teamName.append(name[2] + name[3] + name[4][:-2])
    elif (name[2][-1] == 'A' or name[2][-1] == 'C' or name[2][-1] =='P'):
        
        teamName.append(name[2][:-2])
    else:
        teamName.append(name[2][:-3])

for team in theTeams [2:]:   
    name = re.split('(\d+)',team)

    if(name[2] == 'Philadelphia '):
        teamWins.append(float(name[5][:-2]))
    else:
        teamWins.append(float(name[3][:-2]))    

for team in theTeams [2:]:   
    name = re.split('(\d+)',team)

    if(name[2] == 'Philadelphia '):
        teamLosses.append(float(name[5][2:]))
    else:
        teamLosses.append(float(name[3][2:]))    

for team in theTeams [2:]:   
    name = re.split('(\d+)',team)

    if(name[2] == 'Philadelphia ' or name[6] == '-'):
        teamOffense.append(float(name[9][2:] + '.' + name[11][:-3]))
    else:
        teamOffense.append(float(name[7][2:] + '.' + name[9][:-3]))    

for team in theTeams [2:]:   
    name = re.split('(\d+)',team)

    if(name[2] == 'Philadelphia '):
        teamDefense.append(float(name[11][-3:] + '.' + name[13][:2]))
    elif(name[6] == '-'):
        teamDefense.append(float(name[11][-3:] + '.' + name[13]))
    else:
        teamDefense.append(float(name[9][-3:] + '.' + name[11][:2]))    

for team in theTeams [2:]:   
    name = re.split('(\d+)',team)

    if(name[2] == 'Philadelphia '):
        teamRating.append(float(name[13][2] + '.' + name[15][2:]))
    elif(name[6] == '-' and name[18] == '-'):
        teamRating.append(float(name[14] + name[15] + '.' + name[17]))
    elif(name[6] == '-'):
        teamRating.append(float(name[14] + name[15] + '.' + name[17][:-1]))
    elif(name[14] == '-'):
        teamRating.append(float(name[11][-1] + '.' + name[13]))
    else:
        teamRating.append(float(name[11][2:] + '.' + name[13][:2]))    

i = 0
for team in theTeams [2:]:
    projectedWins.append(int(((teamRating[i]/2+105)**15.3)/(((teamRating[i]/2+105)**15.3)+((105.0-teamRating[i]/2)**15.3))*(82 - (teamWins[i] + teamLosses[i])) + teamWins[i]))
    i = i + 1





class Team:
    def __init__(self, theTeamName, theTeamWins, theTeamLosses, theTeamOffense, theTeamDefense, theTeamRating, theProjectedWins):
        self.theTeamName = theTeamName
        self.theTeamWins = theTeamWins
        self.theTeamLosses = theTeamLosses
        self.theTeamOffense = theTeamOffense
        self.theTeamDefense = theTeamDefense
        self.theTeamRating = theTeamRating
        self.theProjectedWins = theProjectedWins
        

allTeams = []
i = 0      


for team in theTeams [2:]:
    newTeam = Team(teamName[i], teamWins[i], teamLosses[i], teamOffense[i], teamDefense[i], teamRating[i], projectedWins[i])
    allTeams.append(newTeam)
    i = i + 1

import json


def write_json(data, filename="teamdata.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


with open ("teamdata.json") as json_file:
    data = json.load(json_file)
    temp = data["data"]
    for team in allTeams:
        y = {"Name": team.theTeamName, "Wins": team.theTeamWins, "Losses": team.theTeamLosses, "Offense": team.theTeamOffense, "Defense": team.theTeamDefense, "Rating": team.theTeamRating, "Projected Wins": team.theProjectedWins}
        temp.append(y)
write_json(data) 
