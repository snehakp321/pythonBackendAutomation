import requests
from utilities.configurations import *
from utilities.resources import *


def after_scenario(context,scenario):
    if "Library" in scenario.tags:
        deletebookurl = getConfig()["API"]['endpoint'] + ApiResources.deleteBook
        deletebook_response = requests.delete(deletebookurl, json={"ID": "" + context.bookID + ""}, headers=context.headers)
        deletebook_response = deletebook_response.json()
        print(deletebook_response)
        assert deletebook_response["msg"] == "book is successfully deleted"
        deletebook_response == 200