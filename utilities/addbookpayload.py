from utilities.configurations import getQuery


def addBookPayload(isbn,aisle):
    body = {
        "name": "Learn Cypress Automation with JS",
        "isbn": isbn,
        "aisle": aisle,
        "author": "John Doe"}
    return body


def buildpayloadfromdb(query):
    addbody = {}
    tp = getQuery(query)
    addbody['name'] = tp[0]
    addbody['isbn'] = tp[1]
    addbody['aisle'] = tp[2]
    addbody['author'] = tp[3]
    return addbody