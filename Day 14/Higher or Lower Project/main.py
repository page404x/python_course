import art
import game_data
import random

print(art.logo)
first = random.randint(0,49)
print(game_data.data[first]["name"])
print(art.vs)
second = random.randint(0,49)
print(game_data.data[second]["name"])