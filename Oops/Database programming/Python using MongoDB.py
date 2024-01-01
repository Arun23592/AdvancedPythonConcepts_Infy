conn_obj = MongoClient('mongodb://hostname:portnumber/')
from pymongo import MongoClient
#Establishing MongoDB connection
conn_obj = MongoClient('mongodb://localhost:27017/')
print(type(conn_obj))
conn_obj = MongoClient(hostname, portnumber)

# Fetching list of databases and collections:
from pymongo import MongoClient
conn_obj = MongoClient('mongodb://localhost:27017/')
#Fetches the list of databases
db_list = conn_obj.list_database_names()
print(db_list)
database_obj = conn_obj['ETA']
#Fetches the list of collections under 'ETA' database
col_list = database_obj.list_collection_names()
print(col_list)


# Inserting data  into collections:


from pymongo import MongoClient
conn_obj = MongoClient('mongodb://localhost:27017/')
database_obj = conn_obj['ETA']
collection_obj = database_obj['student']
document_list = [
    {'Name':'Kelley','Regd_id':'2','Age':21,'Sex':'M'},
    {'Name':'Hannah','Regd_id':'3','Age':18,'Sex':'F'},
    {'Name':'Ravi','Regd_id':'4','Age':22,'Sex':'M'},
    {'Name':'Rachel','Regd_id':'5','Age':26,'Sex':'F'},
    {'Name':'Esther','Regd_id':'6','Age':19,'Sex':'F'}
]
returnval = collection_obj.insert_many(document_list)
print(returnval.inserted_ids)


# Retrieving documents from collection
from pymongo import MongoClient
conn_obj = MongoClient('mongodb://localhost:27017/')
database_obj = conn_obj['ETA']
collection_obj = database_obj['student']
#Fetching the first document
print('Find One Document:')
doc = collection_obj.find_one()
print(doc)
#Fetching all the documents
print('Find All Documents:')
docs = collection_obj.find()
for doc in docs:
    print(doc)


# Projection (Filtering Columns)

from pymongo import MongoClient
conn_obj = MongoClient('mongodb://localhost:27017/')
database_obj = conn_obj['ETA']
collection_obj = database_obj['student']
docs = collection_obj.find({},{'_id':0,'Name':1,'Age':1})
for doc in docs:
    print(doc)
