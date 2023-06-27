import datetime

from pymongo import MongoClient
import pymongo


client = MongoClient('mongodb://localhost:27017/')
db = client['test_database']

stack1 =\
{
    'name': 'customer1',
    'pip': ['python', 'java', 'go'],
    'info': {'os': 'mac'},
    'data': datetime.datetime.utcnow()
}

stack2 =\
{
    'name': 'customer2',
    'pip': ['python', 'java'],
    'info': {'os': 'mac'},
    'data': datetime.datetime.utcnow()
}

from bson.objectid import ObjectId

db_stacks = db.stacks
stack_id = db_stacks.insert_one(stack1).inserted_id
print(stack_id, type(stack_id))

print(db_stacks.find_one({'_id': stack_id}))
str_stack_id = "5ac87a9dc23edc1b7d9b4d68"
print(db_stacks.find_one({'_id': ObjectId(str_stack_id)}))
print(db_stacks.find_one({'name' : 'customer1'}))

for stack in db_stacks.find():
    print(stack)

now = datetime.datetime.utcnow()

for stack in db_stacks.find({'date': {'$lt': now}}):
    print(stack)


db_stacks.find_one_and_update(
    {'name': 'customer1'},
    {'$set': {'name': 'YYY'}})
print(db_stacks.find_one({'name': 'YYY'}))
db_stacks.delete_one({'name' : 'YYY'})
print(db_stacks.find_one({'name': 'YYY'}))
