from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    
    def __init__(self): # Hard coded the user/password
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        #self.client = MongoClient('mongodb://localhost:38854') # This is activated without Authorization
        self.client = MongoClient('mongodb://%s:%s@localhost:38854/?authMechanism=DEFAULT&authSource=AAC'%('aacuser', '5678'))
        self.database = self.client["AAC"]
        
    ### Main Functions down below ### 
    #################################
    
    def create(self, data):
        if data is not None:
            self.database.animals.insertOne(data) # This would be used to insert a single entry...
            return bool(True)
        else:
            #raise Exception("Nothing to create, because parameter is empty...")
            return bool(False)
            
    def read(self, data):
        if data is not None:
            return self.database.animals.find_one(data, {'_id':False}) # returns the cursor, excluding the "_id" attribute
        else:
            raise Exception("Nothing to read, because parameter is empty...")  
            
    def update(self, search, data):
        if data is not None:
            if self.database.animals.find_One(search) is None:
                raise Exception("Nothing to replace, search returned Null...")
            else:
                cursor = self.database.find_one(search)
                self.database.animals.updateOne(search, data)
                for item in cursor:
                    return item
        else:
            raise Exception("Nothing to update, because parameter is empty...")
                  
#     def deleteMany(self, search, data): # not sure how indepth our program is suppose to be. 
#         if data is not None:    # wrote the bases of it.
#             print("Deleting many items")
#         else:
#             raise Exception("Nothing to delete, because parameter is empty...")
            
    def delete(self, search):
        # Check if data is Null...
        if data is not None:
                  # Check if data entry actually exists..
            if self.database.animals.find_one(search) is None:
                Exception("Nothing to delete, search returned Null...")
            else:
                cursor = self.database.animals.findOne(search) 
                self.database.animals.delete_one(search)
                for item in cursor:
                    return item
        else:
            raise Exception("Nothing to delete, because parameter is empty...")