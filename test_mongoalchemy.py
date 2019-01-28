from flask import Flask, jsonify, json
from flask_mongoalchemy import MongoAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
ma = Marshmallow(app)

app.config['DEBUG'] = True
app.config["MONGOALCHEMY_DATABASE"] = "todo_db"
app.config["MONGOALCHEMY_CONNECTION_STRING"] = "mongodb://mongouser:mongouser1@ds153394.mlab.com:53394/todo_db"

db = MongoAlchemy(app)

class TodoList(db.Document):
    title = db.StringField()
    id = db.IntField()

class ItemList(db.Document):
    id = db.IntField()
    title = db.StringField()
    id = db.IntField()

class TodoSchema(ma.Schema):
    class Meta:
        model = TodoList

todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)

##################################
# SPECIAL CONSTRUCTION an object serialization/deserialization
# to be continue in ver 2.0
##################################



# testing service
@bp.route("/")
@bp.route("/index")
def start():
    message = {
        'Version without MongoDB': 'v1.0.0',
        'status': '200',
        'message': 'Hi! The request has succeeded. Let`s go...!'
    }
    response = jsonify(message)
    return response

##################################
# TODO LIST endpoints ###########
#################################

# 1. HTTP endpoint to create a new Todo list
@app.route('/<string:new>/new')
def createNewToDo(new):
    todo = TodoList(title = new)
    todo.save()
    return jsonify({"message": "ToDo list: " + todo.title + " saved."})

# 3. HTTP endpoint to fetch a list of all existing Todo lists
@app.route("/list")
def getAllToDos():
    todos = TodoList.query.all()
    respons = todos_schema.dump(todos)
    return jsonify(respons.data)

# 4. HTTP endpoint to modify an existing Todo list
@app.route('/<string:old>/<string:new>/update', methods=['PATCH'])
def updateExistingToDo(old, new):
    todo = TodoList.query.filter(TodoList.title == old).first()
    todo.title = new
    todo.save()
    return jsonify({"message": "updated to: " + todo.title})

# 5. HTTP endpoint to delete an existing Todo list
@app.route("/<string:old>/delete" , methods=["DELETE"])
def deleteToDoById(old):
    todo = TodoList.filter(TodoList.title == old)
    todo.remove()
    return jsonify({"message": "Todo list: " + todo._id + " removed!"})

##################################
# ITEMS endpoints ###############
#################################
# ver api.2

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
