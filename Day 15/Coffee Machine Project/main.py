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

def resource_remaining():
    print(f"Water : {resources['water']}ml")
    print(f"Milk : {resources['milk']}ml")
    print(f"Coffee : {resources['coffee']}g")
    print(f"Money : ${money}")

def money_conversion(num_quarter, num_dimes, num_nickels, num_pennies):
    quarters_dollar = num_quarter * 0.25
    dimes_dollar = num_dimes * 0.1
    nickles_dollar = num_nickels * 0.05
    pennies_dollar = num_pennies * 0.01
    dollar = quarters_dollar + dimes_dollar + nickles_dollar + pennies_dollar
    return dollar

money = 0

user_input = input("What Would You Like? (Espresso/Latte/Cappucino)? ").lower()
if user_input == "report":
   resource_remaining()
elif user_input == "espresso":




#TODO 2 - Turn off Machine (OFF)
#TODO 3 - Print Report

#