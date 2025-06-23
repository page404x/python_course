import art
import random

print(art.logo)

cards = {
    "AS":11,
    "2" :2,
    "3" :3,
    "4" :4,
    "5" :5,
    "6" :6,
    "7" :7,
    "8" :8,
    "9" :9,
    "10":10,
    "Jack":10,
    "Queen":10,
    "King":10
}

def deal_card():
    new_card = {}
    key = random.choice(list(cards.keys()))
    new_card[key] = cards[key]
    return new_card

def card_result(card):
    return sum(card.values())

def card_winner(c_result, p_result):
    if c_result > 21:
        c_result %= 21
    if p_result > 21:
        p_result %= 21
    if c_result < p_result:
        winner = "Player Win"
    else:
        winner = "Player Lose"
    return winner

cpu_card = {}

c_card = deal_card()
print(c_card)
key = c_card.keys()
value = c_card.values()
card_cpu[key] = value
print(f"{key} {value} {card_cpu}" )


#player_card = deal_card()+deal_card()


#print(f"CPU Card : {cpu_card[0]} and {cpu_card[2]} ")
#print(f"Player Card : {player_card[0]} and {player_card[2]}")

#print(sum(cpu_card.values()))
#print(sum(player_card.values()))
#deal_again = "y"
#while deal_again == "y":
#    deal_again = input("Do you want to deal again? ").lower()
#    if deal_again == "y":
#        player_card += deal_card()
#        print(f"Player Cards : {list(player_card.keys())}")
#    player_result = card_result(player_card)
#    if player_result >= 21:
#        deal_again = "n"

#cpu_result = card_result(cpu_card)
#player_result = card_result(player_card)

#result = card_winner(cpu_result, player_result)
#print(f"And The Result is : {result}")



