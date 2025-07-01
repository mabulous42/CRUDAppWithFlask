from flask import Flask
from flask_scss import Scss


app = Flask(__name__)


@app.route("/")
def home():
    return "My first Flask App"




if __name__ == '__main__' :
    app.run(debug=True)