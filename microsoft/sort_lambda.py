presenters = [
    {'name': 'Suan', 'age': 18},
    {'name': 'Christopher', 'age': 20}
]
presenters.sort(key=lambda item: item['name'])
print(presenters)
print()
print('*' * 20)
print()
presenters.sort(key=lambda item: len(item['name']))
print(presenters)
