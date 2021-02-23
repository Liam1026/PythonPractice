import json

# Create a dictionary object
person_dict = {'first': 'Will', 'last': 'Hope'}
person_dict['City'] = 'Shanghai'

language_list = ['Go', 'Python', 'Rust']
person_dict['Languages'] = language_list

person_json = json.dumps(person_dict)

staff_dict = {}
staff_dict['Program Learner'] = person_dict
staff_json = json.dumps(staff_dict)

print(person_json)
print(staff_json)
