def format_name(f_name, l_name):
    f_name = f_name.title()
    l_name = l_name.title()
    full_name = f_name + " " + l_name
    return full_name

full_name = input("What is your full name ?").split()

print(format_name(full_name[0], full_name[1]))