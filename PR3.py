import random

class army:                             
    def __init__(self, num, team):
        self.num = num
        self.team = team
    
    def follow_hero(self, hero):
        print(f"Воин {self.num} следует за героем {hero.team}")

class Hero:                             
    def __init__(self, team):
        self.team = team
        self.level = 1
        
    def increase_level(self):           
        self.level += 1
        
        
        
    

team1_hero = Hero(1)       
team2_hero = Hero(2)

team1_army = []          
team2_army = []

for i in range(100):
    team = random.choice([1, 2])
    
    soldier = army(i + 1, team)

    if team == 1:
        team1_army.append(soldier)
    else:
        team2_army.append(soldier)

print(f"Количество солдат в команде 1: {len(team1_army)}")
print(f"Количество солдат в команде 2: {len(team2_army)}")

if len(team1_army) > len(team2_army):
    team1_hero.increase_level()
    print(f"Герой команды 1 повысился до уровня {team1_hero.level}")
else:
    team2_hero.increase_level()
    print(f"Герой команды 2 повысился до уровня {team2_hero.level}")

follow = random.choice(team1_army)
follow.follow_hero(team1_hero)




