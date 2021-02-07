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
def get_inital(name):
    inital = name[0:1].upper()
    return inital

first_name = input('What\'s your first name? ')
first_name_inital = get_inital(first_name)
middle_name = input('Enter your middle name: ')
middle_name_inital = get_inital(middle_name)
last_name = input('Enter your last name: ')
last_name_inital = get_inital(last_name)
print('Your initals are: ' + first_name_inital + middle_name_inital + last_name_inital)
