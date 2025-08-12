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
#user_input = input("What Would You Like? (Espresso/Latte/Cappucino? ").lower()

def coffee_ingredient(choice):
    coffee = MENU[choice]["ingredients"]["coffee"]
    return coffee

def water_ingredient(choice):
    water = MENU[choice]["ingredients"]["water"]
    return water

def milk_ingredient(choice):
    milk = MENU[choice]["ingredients"]["milk"]
    return milk

def coffee_cost(coffee):
    cost = MENU[coffee]["cost"]
    return cost

def resource_remaining(coffee, water, milk):
    remaining_water = resources["water"]


#TODO 2 - Turn off Machine (OFF)
#TODO 3 - Print Report

#