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

def resource_print():
    print(f"Water : {resources['water']}ml")
    print(f"Milk : {resources['milk']}ml")
    print(f"Coffee : {resources['coffee']}g")
    print(f"Money : ${total_money}")

def money_conversion(num_quarter, num_dimes, num_nickels, num_pennies):
    quarters_dollar = int(num_quarter)* 0.25
    dimes_dollar = int(num_dimes) * 0.1
    nickles_dollar = int(num_nickels) * 0.05
    pennies_dollar = int(num_pennies) * 0.01
    fun_dollar = quarters_dollar + dimes_dollar + nickles_dollar + pennies_dollar
    return round(fun_dollar,2)

def input_money():
    num_quarters = input("How many quarters: ")
    num_dimes = input("How many dimes: ")
    num_nickles = input("How many nickles: ")
    num_pennies = input("How many pennies : ")
    return num_quarters, num_dimes, num_nickles, num_pennies

def check_resources(choice, not_milk):
    fun_water = resources["water"] - MENU[choice]["ingredients"]["water"]
    fun_coffee = resources["coffee"] - MENU[choice]["ingredients"]["coffee"]
    if not not_milk:
        fun_milk = resources["milk"] - MENU[choice]["ingredients"]["milk"]
    else:
        fun_milk = resources["milk"]
    fun_money = MENU[choice]["cost"]
    return fun_water, fun_coffee, fun_milk, fun_money

total_money = 0
repeat = True
while repeat :
    user_input = input("What Would You Like? (Espresso/Latte/Cappuccino)? ").lower()
    no_milk = False
    if user_input == "report":
        resource_print()
    elif user_input == "off":
        print("Turning OFF Machine")
        repeat = False
    else:
        try:
            if user_input == "espresso":
                no_milk = True
            water, coffee, milk, add_money = check_resources(user_input, no_milk)
            if water >= 0 and coffee >= 0 and milk >= 0:
                q, d, n, p = input_money()
                dollar = money_conversion(q, d, n, p)
                changes = round(dollar - MENU[user_input]["cost"],2)
                if changes >= 0:
                    print(f"Here is ${changes} in changes")
                    print(f"Here is your {user_input} Enjoy!")
                    resources["water"] = water
                    resources["coffee"] = coffee
                    resources["milk"] = milk
                    total_money += add_money
                else:
                    print("your money is not enough")
            else:
                print(f"Resources has been depleted to make {user_input}, please choose another one")
        except KeyError:
            print("Please input the correct choice")
#