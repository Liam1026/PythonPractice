# Ask for someone name and return the initials

# first_name = input('What\'s your first name? ')
# first_name_inital = first_name[0:1]


# middle_name = input('Enter your middle name: ')
# middle_name_inital = middle_name[0:1]

# last_name = input('Enter your last name: ')
# last_name_inital = last_name[0:1]

# last_name = input('Enter your last name: ')
# print('Your initals are: ' + first_name_inital + middle_name_inital + last_name_inital)

# inital Function to get the first letter of the name
def get_inital(name, force_uppercase=True):
    if force_uppercase:
        inital = name[0:1].upper()
    else:
        inital = name[0:1]
    return inital

first_name = input('What\'s your first name? ')
first_name_inital = get_inital(first_name, False)
# first_name_inital = get_inital(name=first_name, force_uppercase=False)
print('Your inital is: ' + first_name_inital )