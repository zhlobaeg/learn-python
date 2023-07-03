def get_team_speed(team):
    num_players = len(team['players'])
    total_speed = 0
    for player in team['players']:
        total_speed += player['speed']
    return total_speed / num_players

def get_team_strength(team):
    total_strength = 0
    for player in team['players']:
        total_strength += player['strength']
    return total_strength

def get_team_names(team):
    names = []
    for player in team['players']:
        names.append(player['name'])
    return names

def add_team_strength(team, points):
    for player in team['players']:
        player['strength'] += points


player1 = {
    'name': 'Bob',
    'speed': 15,
    'strength': 10
}

player2 = {
    'name': 'John',
    'speed': 17,
    'strength': 13
}

player3 = {
    'name': 'Jenny',
    'speed': 16,
    'strength': 12
}

player4 = {
    'name': 'Bill',
    'speed': 14,
    'strength': 14
}


team1 = {
    'name': 'coolteam',
    'players': [player1, player2]
}

team2 = {
    'name': 'superteam',
    'players': [player3, player4]
}

#print(team1['players'][0]['name'])
#print(team2['players'][1]['speed'])

team_speed = get_team_speed(team1)
team_speed2 = get_team_speed(team2)
#print(team_speed, team_speed2)

team_strength = get_team_strength(team1)
team_strength2 = get_team_strength(team2)
t_s = team_strength2 + team_strength
#print(t_s)
teamnames = get_team_names(team1)
teamnames2 = get_team_names(team2)
#print(teamnames, teamnames2)

add_team_strength(team1, 21)
print(team1)