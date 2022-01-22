import json

#loads- string
#load- file object

coursespath="/Users/snehaprakash/Desktop/Python Backend Auto/courses.json"
complexjsonpath="/Users/snehaprakash/Desktop/Python Backend Auto/ComplexJson.json"
path="/Users/snehaprakash/Desktop/Python Backend Auto/Document.json"

with open(coursespath) as read:
    data =json.load(read)
    print(type(data))
    print((data))
    print(data['courses'][1]["title"])
    print(data["dashboard"]["website"])
#print cypress in console and access website
#get price of webdriver io

    for item in data["courses"]:
        if item["title"]=="webdriver.io":
            print(item["price"])
            assert item['price']==300