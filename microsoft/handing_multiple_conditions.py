# province = input('Where are you from? ')
# # if province == 'ShangHai':
# #     tax = 0.05
# # elif province == 'Beijing':
# #     tax = 0.05
# # if province == 'Shanghai' or province == 'Beijing':
# if province in('Shanghai', 'Beijing'):
#     tax = 0.05
# elif province == 'Hangzhou':
#     tax = 0.08
# else:
#     tax = 0.15
# print('Tax is : ', tax)


country = input('What country do you live in? ')

if country == 'China':
    province = input('What province or state do you livein ? ')
    if province == 'Beijing':
        tax = 0.08
    elif province in('Shanghai', 'Hangzhou', 'Suzhou'):
        tax  = 0.06
    elif province == 'Chengdu':
        tax = 0.02
    else:
        tax = 0.15
else:
    tax = 0

print('Tax is: ', tax)
