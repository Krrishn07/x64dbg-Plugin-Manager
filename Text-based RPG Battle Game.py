import random

class Player:
    def __init__(self):
        self.health = 100
        self.attack_power = 20

class Monster:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

def battle(player, monster):
    while player.health > 0 and monster.health > 0:
        player_attack = random.randint(1, player.attack_power)
        monster_attack = random.randint(1, monster.attack_power)
        
        print(f"You attack the {monster.name} for {player_attack} damage!")
        monster.health -= player_attack
        
        if monster.health <= 0:
            print(f"You defeated the {monster.name}!")
            break
        
        print(f"The {monster.name} attacks you for {monster_attack} damage!")
        player.health -= monster_attack
        
        print(f"Your health: {player.health}, {monster.name}'s health: {monster.health}\n")
        
    if player.health <= 0:
        print("Game Over! You were defeated by the monster.")
    else:
        print("Congratulations! You won the battle!")

# Create the player
player = Player()

# Define some monsters
monsters = [
    Monster("Goblin", 30, 10),
    Monster("Orc", 50, 15),
    Monster("Dragon", 100, 25)
]

# Game loop
while player.health > 0:
    input("Press Enter to encounter a random monster...")
    random_monster = random.choice(monsters)
    print(f"You encounter a {random_monster.name}!\n")
    battle(player, random_monster)
