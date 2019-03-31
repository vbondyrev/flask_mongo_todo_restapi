class TodoList:
    '''LIST ALL TO DO TASKS
    '''
    id = ""
    title = ""

    def __init__(self, id, title):
        self.id = id
        self.title = title

    def toJson(self):
        in_json = {"id":self.id, "title":self.title}
        return in_json

toDoList = []

toDoList1 = TodoList(id="1", title="Important And Urgent Tasks")
toDoList2 = TodoList(id="2", title="Important But Not Urgent Tasks")
toDoList3 = TodoList(id="3", title="Not Important But Urgent Tasks")
toDoList4 = TodoList(id="4", title="NotImportant, Not Urgent Task")

toDoList.append(toDoList1.toJson())
toDoList.append(toDoList2.toJson())
toDoList.append(toDoList3.toJson())
toDoList.append(toDoList4.toJson())

class TodoItem(TodoList):
    '''LIST ALL ITEMS TO DO TASKS
    '''
    id_item = ""
    id_todo = ""
    text = ""
    data = ""
    status = ""

    def __init__(self, id_item, id_todo, text, data, status):
        self.id = id_item
        self.id_todo = id_todo
        self.text = text
        self.data = data
        self.status = status

    def toJson2(self):
        in_json = {"id_item":self.id_item, "id_todo":self.id_todo, "text":self.text, "data":self.data, "status":self.status}
        return in_json

toDoItemList = []

toDoItemList1 = TodoItem(id_item="1", id_todo="1", text="Crises", data="2019/01/01", status="Done")
toDoItemList2 = TodoItem(id_item="2", id_todo="1", text="Deadlines", data="2019/01/01", status="Done")
toDoItemList3 = TodoItem(id_item="3", id_todo="1", text="Problems", data="2019/01/01", status="Done")
toDoItemList4 = TodoItem(id_item="4", id_todo="1", text="HOT Fix", data="2019/01/01", status="Done")

toDoItemList5 = TodoItem(id_item="1", id_todo="2", text="Relationships", data="2019/01/01", status="Done")
toDoItemList6 = TodoItem(id_item="2", id_todo="2", text="Planning", data="2019/01/01", status="Done")
toDoItemList7 = TodoItem(id_item="3", id_todo="2", text="Recreation", data="2019/01/01", status="Done")

toDoItemList8 = TodoItem(id_item="1", id_todo="3", text="Interruptions", data="2019/01/01", status="Done")
toDoItemList9 = TodoItem(id_item="2", id_todo="3", text="Meetings", data="2019/01/01", status="Done")
toDoItemList10 = TodoItem(id_item="3", id_todo="3", text="Activities", data="2019/01/01", status="Done")

toDoItemList11 = TodoItem(id_item="1", id_todo="4", text="Time Wasters", data="2019/01/01", status="Done")
toDoItemList12 = TodoItem(id_item="2", id_todo="4", text="Pleasant Activities", data="2019/01/01", status="Done")
toDoItemList13 = TodoItem(id_item="3", id_todo="4", text="Trivia", data="2019/01/01", status="Done")

toDoItemList.append(toDoItemList1.toJson2())
toDoItemList.append(toDoItemList2.toJson2())
toDoItemList.append(toDoItemList3.toJson2())
toDoItemList.append(toDoItemList4.toJson2())


class TestTodo():
    '''
    '''
    id = ""
    title = ""
    id_item = ""
    text = ""
    data = ""
    status = ""

    def __init__(self, id, title, id_item, text, data, status):
        self.id = id
        self.title = title
        self.id_item = id_item
        self.text = text
        self.data = data
        self.status = status

    def toJson3(self):
        in_json = {"id":self.id, "title":self.title, "id_item":self.id_item, "text":self.text, "data":self.data, "status":self.status}
        return in_json

testDoItemList = []

testDoItemList1 = TestTodo(id="1", title="Test_title", id_item="1", text="Crises", data="2019/01/01", status="Done")

testDoItemList.append(testDoItemList1.toJson3())
