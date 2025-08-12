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
    quarters_dollar = int(num_quarter)* 0.25
    dimes_dollar = int(num_dimes) * 0.1
    nickles_dollar = int(num_nickels) * 0.05
    pennies_dollar = int(num_pennies) * 0.01
    dollar = quarters_dollar + dimes_dollar + nickles_dollar + pennies_dollar
    return round(dollar,2)

def input_money():
    num_quarters = input("How many quarters: ")
    num_dimes = input("How many dimes: ")
    num_nickles = input("How many nickles: ")
    num_pennies = input("How many pennies : ")
    return num_quarters, num_dimes, num_nickles, num_pennies

money = 0

user_input = input("What Would You Like? (Espresso/Latte/Cappuccino)? ").lower()
if user_input == "report":
   resource_remaining()
else:
    q, d, n, p = input_money()
    dollar = money_conversion(q,d,n,p)
    try:
        changes = dollar - MENU[user_input]["cost"]
        print(f"Here is ${changes} in changes")
        print(f"Here is your {user_input} Enjoy!")
    except KeyError:
        print("Please input the correct choice")





#TODO 2 - Turn off Machine (OFF)
#TODO 3 - Print Report

#