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

    if not task:  # Check if task is empty
        return redirect('/')  # Just redirect back without adding

    todo.append({
        'id': str(uuid.uuid4()),  # Unique identifier
        'task': task,
        'date': date
    })
    save_data(todo)
    return redirect('/')

@app.route('/delete/<id>')
def delete(id):
    todo = load_data()
    todo = [t for t in todo if t['id'] != id]
    save_data(todo)
    return redirect('/')

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    todo = load_data()
    todo_item = next((t for t in todo if t['id'] == id), None) #you can use this method too
    if todo_item == None:
        return render_template("/")
    # for t in todo:
    #     if t["id"] == id:
    #         todo = t

    if request.method == 'POST':
        # Find and update the item within the original list
        for t in todo:
            if t["id"] == id:
                t['task'] = request.form['task']
                t['date'] = datetime.now().strftime("%Y-%m-%d")
                break
        save_data(todo)  # Save the entire list, not just one item
        return redirect("/")
    else:
        return render_template('edit.html', todo=todo_item)






if __name__ == '__main__' :
    app.run(debug=True)