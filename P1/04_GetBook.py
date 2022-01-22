import requests
import json

response= requests.get('http://216.10.245.166/Library/GetBook.php',
             params={"AuthorName":"John Mark"},)

# print(response.text)
# print(type(response.text))
# dict_resp= json.loads(response.text) #here it is in list not dictionary
# print(type(dict_resp))
# print(dict_resp[0]['isbn'])

print(type(response.json())) #to retrive list
assert(response.status_code)==200
assert(response.headers["Content-Type"])=='application/json;charset=UTF-8'
print(response.cookies)

for item in response.json():
    print(item["aisle"])
    if item["aisle"] == '22753':
        print(item["book_name"])
        break

expectedBook={
        "book_name": "Learn Appium Automation11",
        "isbn": "bcdef",
        "aisle": "22753"
    }
assert item==expectedBook

