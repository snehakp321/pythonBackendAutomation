import json

courses = '{"name": "sneha","languages": ["Python","Java"]}'

# Loads method parse json string and it returns dictionary

dict_courses=json.loads(courses)
print(type(dict_courses))
print(dict_courses)
print(dict_courses["name"])
print(dict_courses["languages"][0])