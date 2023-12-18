from flask import request
from flask import json


def get_data():
    import http.client
    conn = http.client.HTTPSConnection("yts.unblockit.lat")
    conn.request("GET", "/api/v2/list_movies.json?limit=10")
    res = conn.getresponse()
    data = res.read()
    return json.loads(data.decode("utf-8"))


def process():
    data=get_data()
    i=0
    data1=data["data"]["movies"][i]
    return data1

 