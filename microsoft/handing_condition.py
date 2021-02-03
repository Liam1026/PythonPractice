# price = 0.99

# if price >= 1:
#     tax = 0.07
# else:
#     tax = 0

# print(tax)

price = input('How much did you pay? ')
price = float(price)

if price >= 1.0:
    tax = .07
else:
    tax = 0

print('Tax is: ' + str(tax))

country = input('Enter the name of your home country: ')

if country.lower() =='china':
    print(' A Chinese!!')
else:
    print("You are not from China!")