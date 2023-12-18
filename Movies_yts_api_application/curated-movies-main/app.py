from flask import Flask

from flask import render_template
from flask import request
from flask import json
from model import process_data 
from model import movie_details
import urllib3
import urllib.parse
import http
import requests

app = Flask(__name__)



@app.route('/', methods=['GET'])
def index():
    return render_template("index.html", data=movie_details.process() ,action=movie_details.action(), comedy=movie_details.comedy(), adventure=movie_details.adventure(), animation=movie_details.animation(), horror=movie_details.horror(), romantic=movie_details.romantic())

@app.route('/search', methods=['GET', 'POST'])
def search():
   if request.method == 'POST':
      query_term = request.form['search-bar']
      limit=50
      api='https://yts.unblockit.app/api/v2/list_movies.json?'
      url=api + urllib.parse.urlencode({'query_term': query_term , 'limit': limit})
      data=requests.get(url).json()
      movie_found=data["data"]["movie_count"]
      if movie_found!=0:
          data2=data["data"]["movies"]
          return render_template("search.html", search1 = data2, mf= movie_found)
      else:
          return render_template("notfound1.html")

@app.route('/filter', methods=['GET', 'POST'])
def filter():
   if request.method == 'POST':
      rating=request.form['rating']
      genre=request.form['genre']
      sort_by=request.form['sort_by']
      limit=50
      api='https://yts.unblockit.app/api/v2/list_movies.json?'
      url=api + urllib.parse.urlencode({ 'minimum_rating': rating , 'genre': genre ,'limit': limit ,'sort_by': sort_by})
      data=requests.get(url).json()
      movie_found=data["data"]["movie_count"]
      if movie_found!=0:
          data2=data["data"]["movies"]
          return render_template("filter.html", search1 = data2, mf= movie_found)
      else:
          return render_template("notfound.html")


@app.route('/movies_details', methods=['GET', 'POST'])
def movies_details():
   if request.method == 'POST':
      movid=request.form['mid']
      api='https://yts.unblockit.app/api/v2/movie_details.json?'
      url=api + urllib.parse.urlencode({ 'movie_id': movid })
      d=requests.get(url).json()
      mov=d["data"]["movie"]
      return render_template("movies_details.html", md = mov)
     



if __name__ == '__main__':
    app.run(debug=True)