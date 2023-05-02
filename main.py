from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://Aarish:aarishMohammed@cluster0.ukpq5xk.mongodb.net/test"
db = PyMongo(app).db

@app.route("/")
def hello_world():
    db.db.inventory.insert_one({"A": 1})
    return "<p>Hello, World!</p>"


app.run(debug=True)