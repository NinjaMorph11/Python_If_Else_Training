print("How many mice do you have?")
nummice = input()

try:
    if int(nummice) >= 4:
        print("That's alot of cats")
    else:
        print("That's not alot")
except ValueError:
    print("That's not a numerical value for this question")
