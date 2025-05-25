import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

count = len(letters)-1
huruf =[]
for letter in range(1, nr_letters+1):
    index = random.randint(0,count)
    huruf.append(letters[index])

count = len(symbols)-1
symbol=[]
for letter in range(1, nr_symbols+1):
    index = random.randint(0,count)
    symbol.append(symbols[index])

count = len(numbers)-1
number=[]
for letter in range(1, nr_numbers+1):
    index = random.randint(0, count)
    number.append(numbers[index])

full_pass=huruf+symbol+number
print("Your password is : ")
print(*full_pass,sep='')
random.shuffle(full_pass)
print(*full_pass,sep='')
