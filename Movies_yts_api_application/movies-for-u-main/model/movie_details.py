from flask import request
from flask import json


def get_data():
    import http.client
    conn = http.client.HTTPSConnection("yts.unblockit.onl")
    conn.request("GET", "/api/v2/list_movies.json?limit=50&sort_by=rating")
    res = conn.getresponse()
    data = res.read()
    return json.loads(data)

def process():
    data=get_data()
    data1=data["data"]["movies"]    
    return data1


def get_action_movies():
    import http.client
    conn = http.client.HTTPSConnection("yts.unblockit.onl")
    conn.request("GET", "/api/v2/list_movies.json?genre=action&limit=50&minimum_rating=8&sort_by=year")
    res = conn.getresponse()
    action = res.read()
    return json.loads(action)


def action():
    action=get_action_movies()
    action=action["data"]["movies"]    
    return action    


def get_comedy_movies():
    import http.client
    conn = http.client.HTTPSConnection("yts.unblockit.onl")
    conn.request("GET", "/api/v2/list_movies.json?genre=comedy&limit=50&minimum_rating=8&sort_by=year")
    res = conn.getresponse()
    data = res.read()
    return json.loads(data)


def comedy():
    data=get_comedy_movies()
    comedy=data["data"]["movies"]    
    return comedy   


def get_horror_movies():
    import http.client
    conn = http.client.HTTPSConnection("yts.unblockit.onl")
    conn.request("GET", "/api/v2/list_movies.json?genre=horror&limit=50&minimum_rating=7&sort_by=year")
    res = conn.getresponse()
    data = res.read()
    return json.loads(data)


def horror():
    data=get_horror_movies()
    horror=data["data"]["movies"]    
    return horror    



def get_animation_movies():
    import http.client
    conn = http.client.HTTPSConnection("yts.unblockit.onl")
    conn.request("GET", "/api/v2/list_movies.json?genre=animation&sort_by=year&minimum_rating=8&limit=50")
    res = conn.getresponse()
    data = res.read()
    return json.loads(data)


def animation():
    data=get_animation_movies()
    animation=data["data"]["movies"]    
    return animation  





def get_adventure_movies():
    import http.client
    conn = http.client.HTTPSConnection("yts.unblockit.onl")
    conn.request("GET", "/api/v2/list_movies.json?genre=adventure&sort_by=year&minimum_rating=8&limit=50")
    res = conn.getresponse()
    data = res.read()
    return json.loads(data)


def adventure():
    data=get_adventure_movies()
    adventure=data["data"]["movies"]    
    return adventure 

def get_romantic_movies():
    import http.client
    conn = http.client.HTTPSConnection("yts.unblockit.onl")
    conn.request("GET", "/api/v2/list_movies.json?genre=romance&sort_by=year&minimum_rating=8&limit=50")
    res = conn.getresponse()
    data = res.read()
    return json.loads(data)


def romantic():
    data=get_romantic_movies()
    romantic=data["data"]["movies"]    
    return romantic     




    