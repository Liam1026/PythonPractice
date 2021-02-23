def sorter(item):
    return item['age']


presenters = [
    {'name': 'Susan', 'age': 18},
    {'name': 'Christopher', 'age': 20}
]

# sort depend function sorter 
presenters.sort(key=sorter)
print(presenters)
