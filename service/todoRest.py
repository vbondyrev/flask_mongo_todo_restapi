from flask import Blueprint, Flask, request, Response, jsonify
from app.models import TodoList, TodoItem, toDoList, toDoItemList, TestTodo, testDoItemList

blueprint = Blueprint('mytodo' , __name__, url_prefix='/todo')

# testing service
@blueprint.route("/")
@blueprint.route("/index")
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

#1. HTTP endpoint to create a new Todo list
@blueprint.route("/new", methods=["POST"])
def createNewToDo():
    item=TodoList(**request.get_json())
    toDoList.append(item.toJson())
    return Response('{"message":"success"}', status=201, mimetype='application/json')

#2. HTTP endpoint to fetch one existing Todo list
@blueprint.route("/<id>")
def findToDoById(id):
    itemToReturn = None
    for item in toDoList:
        if item["id"] == id:
            itemToReturn = item
        else:
            continue
    if itemToReturn == None:
        return Response('{"message":"todo list not found"}', status=404, mimetype='application/json')
    else:
        response = jsonify(itemToReturn)
        response.status_code = 200
        return response

#3. HTTP endpoint to fetch a list of all existing Todo lists
@blueprint.route("/list")
def getAllToDos():
    return jsonify(toDoList)

#4. HTTP endpoint to modify an existing Todo list
@blueprint.route("/edit" , methods=["PATCH"])
def updateExistingToDo():
    item=TodoList(**request.get_json())
    isExist = False
    for i in toDoList:
        if i["id"] == item.id :
            i["title"] = item.title
            isExist = True
            break
    if isExist:
        response = jsonify({"message":"todo list updated successfull"})
        response.status_code = 201
        return response
    else:
        response = jsonify({"message":"todo list not exist"})
        response.status_code = 404
        return response


# 5. HTTP endpoint to delete an existing Todo list
@blueprint.route("/<id>/delete" , methods=["DELETE"])
def deleteToDoById(id):
    itemToDelete = None
    for item in toDoList:
        if item["id"] == id:
            itemToDelete = item
        else:
            continue
    if itemToDelete == None:
        response = jsonify({"message":"todo list not exist"})
        response.status_code = 404
        return response
    else:
        toDoList.remove(itemToDelete)
        response = jsonify({"message":"todo list removed successfully"})
        response.status_code = 200
        return response

##################################
# ITEMS endpoints ###############
#################################

# 6. HTTP endpoint to create a new Todo item in a Todo list
@blueprint.route("/<id>/item/new", methods=["POST"])
def createNewToDoItem():
    item=TodoList(**request.get_json())
    toDoList.append(item.toJson2())
    return Response('{"message":"item added success"}', status=201, mimetype='application/json')

#7. HTTP endpoint to delete a Todo item from a Todo list
@blueprint.route("/<id>/item/<id_item>/delete", methods=["DELETE"])
def deleteToDoItem():
    itemToDelete = None
    for item in toDoItemList:
        if item["id_todo"] == id:
            if item["id_item"] == id_item:
                itemToDelete = item
            else:
                continue
        else:
            continue
    if itemToDelete == None :
        response = jsonify({"message":"item not exist"})
        response.status_code = 404
        return response
    else:
        toDoItemList.remove(itemToDelete)
        response = jsonify({"message":"item removed successfully"})
        response.status_code = 200
        return response

#8. HTTP endpoint to update a Todo item in a Todo list
@blueprint.route("/<id>/item/<id_item>/edit", methods=["PATCH"])
def updateToDoItem():
    return None
