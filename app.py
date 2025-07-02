import json, uuid
from flask import Flask, render_template, url_for, redirect, request
from datetime import datetime

app = Flask(__name__)

def load_data():
    try:
        # loading data from json
        with open('data.json', 'r') as file:
            todo = json.load(file)
            return todo

    except FileNotFoundError:
        print("No saved data found")


# function to save data into json
def save_data(todo):
    # Writing to json
    with open("data.json", "w") as file:
        json.dump(todo, file, indent=4)


@app.route("/")
def home():
    todo = load_data()
    return render_template("index.html", todo=todo)


@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    date = datetime.now().strftime("%Y-%m-%d")
    todo = load_data()
    todo.append({
        'id': str(uuid.uuid4()),  # Unique identifier
        'task': task,
        'date': date
    })
    save_data(todo)
    return redirect('/')




if __name__ == '__main__' :
    app.run(debug=True)