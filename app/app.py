from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from scrape import scrape

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_data_app"
mongo = PyMongo(app)
# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")


@app.route("/")
def index():
    # print('-'*24) 
    # print(NASA)
    NASA = mongo.db.mars.find_one()
    return render_template("index.html", data=NASA)


@app.route("/scrape")
def scraper():
    NASA=scrape() 
    mars = mongo.db.mars 
    mars.update({}, NASA, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
