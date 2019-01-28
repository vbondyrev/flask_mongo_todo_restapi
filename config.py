# Mongo configuration
MONGODB_DB = Mtodo_db()['todo_db']
DEBUG = True
client = MongoClient('mongodb://mongouser:mongouser1@ds153394.mlab.com:53394/todo_db')
