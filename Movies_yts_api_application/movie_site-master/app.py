from flask import Flask

from flask import render_template
from flask import request
from flask import json
from model import process_data 
from model import movie_details


app = Flask(__name__)



@app.route('/', methods=['GET'])
def index():
    return render_template("index.html",data1=process_data.process(), data=movie_details.process())
  
@app.route('/first', methods=['GET'])
def first():
    return render_template("movie-first.html",data1=process_data.process(), data=movie_details.process())



@app.route('/test', methods=['GET'])
def test():
    return render_template("test.html",data1=process_data.process(), data=movie_details.process())


if __name__ == '__main__':
    app.run(debug=True)