# Iterates through string...

# Ask user for string
recipe_name = input("What is the recipe name?")

error = "Your recipe has numbers in it."
has_errors = ""

# Look at each character in string and if it's a number, complain
for letter in recipe_name:
    if letter.isdigit() == True:
        print(error)
        has_errors = "yes"
        break

# give user feedback...
if has_errors != "yes":
    print("you are OK")

