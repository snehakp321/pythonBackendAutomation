import json

coursespath="/Users/snehaprakash/Desktop/Python Backend Auto/courses.json"
complexjsonpath="/Users/snehaprakash/Desktop/Python Backend Auto/ComplexJson.json"

with open(coursespath) as course1:
    data1 =json.load(course1)

with open(complexjsonpath) as course2:
    data2 = json.load(course2)
    print("##################")
    assert(data1==data2)
