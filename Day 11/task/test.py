show_card = []
card = {1: 2, 10: 10}
for key in card:
    if key == 0:
        show_card += "AS"
    if key == 10:
        show_card += "Jack"
    if key == 11:
        show_card += "Queen"
    if key == 12:
        show_card += "King"
    else:
        show_card += str(key + 1)

print (show_card)