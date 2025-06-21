import art
import random
print(art.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card(limit):
    counter = 0
    card = {}
    while counter < limit:
        index = random.randrange(len(cards))
        if index  in card.keys():
            counter = counter
        else:
            card[index] = cards[index]
            counter +=1
    return card

def sum_card_value(card_value):
    return sum(card_value.values())

def showing_card(card):
    show_card =[]

    for key in card:
        if key == 0:
            show_card.append("AS")
        elif key == 10:
            show_card.append("Jack")
        elif key == 11:
            show_card.append("Queen")
        elif key == 12:
            show_card.append("King")
        else:
            show_card.append(str(key+1))
    return show_card


def result(t_c_card, t_p_card):
    if t_c_card > 21 and t_p_card > 21:
        r = "Draw"
    elif t_c_card > 21:
        r = "You Win"
    elif t_p_card > 21:
        r = "You Lose"
    elif t_c_card > t_p_card:
        r = "You Lose"
    elif t_c_card < t_p_card:
        r = "You Win"
    else:
        r = "Draw"
    return r

play = input("Do you want to play black jack (Y/N)? ").lower()
while play=="y":
    cpu_card = deal_card(2)
    total_cpu_card = sum_card_value(cpu_card)
    c_card = showing_card(cpu_card)
#    c_card[1] = "***"
    print(f"CPU Card : {c_card[0]}")

    player_card = deal_card(2)
    total_player_card = sum_card_value(player_card)
    p_card = showing_card(player_card)
    print(f"Player Card : {p_card}")

    deal_more = input("Do you want to deal more card (Y/N)? ").lower()
    while deal_more == "y":
        player_card.update(deal_card(1))
        total_player_card = sum_card_value(player_card)
        print(f"Player Card are: {showing_card(player_card)}")
        if total_player_card <= 21:
            deal_more = input("Do you want to deal more card (Y/N)? ").lower()
        else:
            deal_more = "n"

    while total_cpu_card < 17:
        print("CPU deal more card.... ")
        cpu_card.update(deal_card(1))
        total_cpu_card = sum_card_value(cpu_card)

    print(f"CPU Card are : {showing_card(cpu_card)}")
    print(f"Player Card are: {showing_card(player_card)}")
    print(f"And The Result is : {result(total_cpu_card, total_player_card)}")
    play = input("Do you want to play black jack (Y/N)? ").lower()

