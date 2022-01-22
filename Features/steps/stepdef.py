from behave import *
import requests
from utilities.addbookpayload import addBookPayload, buildpayloadfromdb
from utilities.configurations import *
from utilities.resources import *

# context - assign property of url to it and it can be called anywhere (global) but terminated only when the session ends

@given('the book details which needs to be added to library')
def step_impl(context):
    context.addbookurl = getConfig()["API"]['endpoint'] + ApiResources.addBook
    context.headers = {'Content-Type': 'application/json;charset=UTF-8'}
    context.payload = addBookPayload(262,632)

@given('the book details with {isbn} and {aisle}')
def step_impl(context,isbn,aisle):
    context.addbookurl = getConfig()["API"]['endpoint'] + ApiResources.addBook
    context.headers = {'Content-Type': 'application/json;charset=UTF-8'}
    context.payload = addBookPayload(isbn,aisle)


@when('we execute the AddBook PostAPI method')
def step_impl(context):
    context.response = requests.post(context.addbookurl, json=context.payload, headers=context.headers)


@then('book is successfully added')
def step_impl(context):
    print(context.response.json())
    response_json = (context.response.json())
    context.bookID = response_json['ID']
    print(context.bookID)
    assert response_json['Msg'] == "successfully added"

# session manager, instead of authenticating everytime
@given('I have github auth credentials')
def step_impl(context):
    context.se = requests.session()
    context.se.auth = auth = ('test@123', "test@123")


@when('I hit getrepo API of github')
def step_impl(context):
    context.response = context.se.get(ApiResources.githubrepo)


@then('status code of the response should be {statuscode:d}')
def step_impl(context,statuscode):
    print(context.response.status_code)
    assert context.response.status_code == statuscode

