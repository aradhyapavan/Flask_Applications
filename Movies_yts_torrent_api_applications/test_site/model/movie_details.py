from flask import request
from flask import json


def get_data():
    import http.client
    conn = http.client.HTTPSConnection("yts.unblockit.lat")
    conn.request("GET", "/api/v2/list_movies.json?limit=50")
    res = conn.getresponse()
    data = res.read()
    return json.loads(data)

def process():
    data=get_data()
    data1=data["data"]["movies"]
    return data1


    