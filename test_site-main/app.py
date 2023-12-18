from flask import Flask

from flask import render_template
from flask import request
from flask import json
from model import process_data 
from model import movie_details
import urllib.parse
import http
import requests

app = Flask(__name__)



@app.route('/', methods=['GET'])
def index():
    return render_template("index.html",data1=process_data.process(), data=movie_details.process())

@app.route('/search', methods=['GET', 'POST'])
def search():
   if request.method == 'POST':
      query_term = request.form['search-bar']
      rating=request.form['rating']
      genre=request.form['genre']
      sort_by=request.form['sort_by']
      limit=50
      api='https://yts.unblockit.lat/api/v2/list_movies.json?'
      url=api + urllib.parse.urlencode({'query_term': query_term , 'minimum_rating': rating , 'genre': genre ,'limit': limit ,'sort_by': sort_by})
      data=requests.get(url).json()
      movie_found=data["data"]["movie_count"]
      data2=data["data"]["movies"]
      return render_template("search.html",search1 = data2,mf= movie_found)

  
@app.route('/first', methods=['GET'])
def first():
    return render_template("movie-first.html",data1=process_data.process(), data=movie_details.process())



@app.route('/test', methods=['GET'])
def test():
    return render_template("test.html",data1=process_data.process(), data=movie_details.process())

@app.route('/index1', methods=['GET'])
def index1():
    return render_template("index1.html",data1=process_data.process(), data=movie_details.process())

if __name__ == '__main__':
    app.run(debug=True)