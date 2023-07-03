class Player:
    name = None
    speed = None
    strength = None

    def __init__(self, name, speed, stength):
        self.name = name
        self.speed = speed
        self.strength = stength

    def __str__(self):
        return '<Player {0} {1} {2}>'.format(self.name, self.speed, self.strength)

player1 = Player('Bob', 15, 14)
player2 = Player('John', 14, 10)
player3 = Player('Jimmy', 16, 14)
player4 = Player('Stan', 18, 10)


class Team:
    name = None
    players = []

    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def num_players(self):
        num = len(self.players)
        return num

    def player_names(self):
        names = []
        for player in self.players:
            names.append(player.name)
        return names

    def total_strength(self):
        strength = 0
        for player in self.players:
            strength += player.strength
        return strength

    def get_team_avg_speed(self):
        speed = 0
        for player in self.players:
            speed += player.speed
        return speed / len(self.players)

    def add_team_strength(self, points):
        for player in self.players:
            player.strength += points




team1 = Team('winners')
team1.add_player(player1)
team1.add_player(player2)
team1_strength = team1.total_strength()
team1_avg_speed = team1.get_team_avg_speed()

team2 = Team('coolteam')
team2.add_player(player3)
team2.add_player(player4)
team2_strength = team2.total_strength()
team2.add_team_strength(7)

teams_strength = team1_strength + team2_strength
print(teams_strength)

if team2_strength > team1_strength:
    print(team2.name, 'сильнее')
elif team2_strength < team1_strength:
    print(team1.name, 'сильнее')
else:
    print(team1.name, 'и', team2.name, 'равны')

print(player1.strength)

team1.add_team_strength(6)
print(player1.strength)