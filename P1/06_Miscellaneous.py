import requests

# send and manage cookies through API requests
# redirection and timeout concepts usage in API testing calls
# 302 --> 200 when there is redirection
# 'visit-cookie'
url = "https://rahulshettyacademy.com/"
cookie = {"visit-cookie":"January"}
response = requests.get(url,allow_redirects=False, cookies=cookie,timeout=10)
print(response.history)
print(response.status_code)

# adding cookies to check whether it is consumed or not
res = requests.get("http://httpbin.org/cookies",cookies=cookie)
print(response.history)
print(res.text)

# adding session manager to cookies
se = requests.session()
se.cookies.update({"visit-cookie":"January"})
res = se.get("http://httpbin.org/cookies",cookies={"visit-year":"2022"})
print(response.history)
print(res.text)

# both month and year cookie should be present in the output

# How to send attachments through API calls with python requests library

url = "https://petstore.swagger.io/v2/pet/9843217/uploadImage"
files =  {'file' :open('/Users/snehaprakash/Downloads/Book.jpeg', 'rb')}
r = requests.post(url,files=files)
print(r.status_code)
print(r.text)