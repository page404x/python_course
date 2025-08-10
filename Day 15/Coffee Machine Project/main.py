MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#TODO 1 - User Input (Espresso/Latte/Cappucino)

def resource_remaining(resource_choice):
    remaining = resources[resource_choice]
    return remaining

money = 0

user_input = input("What Would You Like? (Espresso/Latte/Cappucino? ").lower()
if user_input == "report":
    for key in resources:
        remaining = resources[key]
        print(f"{key}: {remaining}")
    print(f"Money: {money}")



#TODO 2 - Turn off Machine (OFF)
#TODO 3 - Print Report

#