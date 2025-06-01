#Function with inputs

def greet(name):
    print(f"Hello {name}")
    print("How do you do?")
    print("Isn't the weather nice?")

greet("reko")


def life_in_weeks(age):
    years_remaining = 90 - age
    weeks_remaining = years_remaining * 12 * 4
    print(weeks_remaining)

age = int(input("Please tell me your age now ? "))
life_in_weeks(age)
