import requests
from utilities.addbookpayload import addBookPayload, buildpayloadfromdb
from utilities.configurations import *
from utilities.resources import *

# add book
addbookurl = getConfig()["API"]['endpoint'] + ApiResources.addBook
headers = {'Content-Type':'application/json;charset=UTF-8'}
addbook_response = requests.post(addbookurl,json=addBookPayload("13","324"),headers=headers)
response_json = (addbook_response.json())
bookID = response_json['ID']
print(bookID)

# # add book using db values
# addbookurldb = getConfig()["API"]['endpoint'] + ApiResources.addBook
# query = "select * from Books;"
# addbookdb_response = requests.post(addbookurldb,json=buildpayloadfromdb(query),headers=headers)
# responsedb_json = (addbookdb_response.json())
# bookIDdb = responsedb_json['ID']
# #print(bookIDdb)

# delete book
deletebookurl = getConfig()["API"]['endpoint']+ ApiResources.deleteBook
deletebook_response = requests.delete(deletebookurl,json={"ID" : ""+bookID+""},headers=headers)
deletebook_response = deletebook_response.json()
assert deletebook_response["msg"] == "book is successfully deleted"
deletebook_response == 200

# Authentication

# Create session manager for API request calls

se = requests.session()
se.auth = auth=('snehakp123',"test@123") # session manager, instead of authenticating everytime
url = "https://api.github.com/user"
github_response = requests.get(url,verify=False, auth=('snehakp123',"test@123"))

url2 = "https://api.github.com/user/repos"
githubuserrepo_response = se.get(url2)
print(githubuserrepo_response.status_code)