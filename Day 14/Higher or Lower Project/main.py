import art
import game_data
import random

def compare_idx():
    obj_list = []
    rand_idx = random.randint(0,49)
    for value in game_data.data[rand_idx].values():
        obj_list.append(value)
    return obj_list

score = 0
lose = False
print(art.logo)
while not lose:
    list_a = compare_idx()
    print(f"Compare A : {list_a[0]}, {list_a[2]}, from {list_a[3]}.")

    print(art.vs)
    list_b = compare_idx()
    print(f"Againts B : {list_b[0]}, {list_b[2]}, from {list_b[3]}.")

    choice = input("who has more followers? Type 'A' or 'B':").lower()
    print("\n" * 20)
    print(art.logo)

    if choice == "a" and (list_a[1] > list_b[1]):
        score += 1
        print(f"You're Right! Current score: {score}")

    elif choice == "b" and (list_b[1] > list_a[1]):
        score += 1
        print(f"You're Right! Current score : {score}")
    else:
        lose = True
        print(f"Sorry, That's wrong. Final Score: {score}")