from art import logo
import os

# TODO-1: Ask the user for input
# Input Data

bid_dict = {}

repeat = "y"
while repeat == "y" :
    print(logo)
    name = input("What is your name? ")
    bid = input("How much is your bid? ")

    # TODO-3: Whether if new bids need to be added
    repeat = input("Do you want to input your bid again [y/n] ?").lower()

    # TODO-2: Save data into dictionary {name: price}
    bid_dict[name]= bid
    #print("\n" * 10)
    os.system('clear')

# TODO-4: Compare bids in dictionary
max_bid = max(bid_dict.values())
max_name = max(bid_dict, key=bid_dict.get)
print(f"Winner goes to {max_name} with the highest bid {max_bid}")








