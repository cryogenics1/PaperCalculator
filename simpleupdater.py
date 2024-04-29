import pymongo
from datetime import datetime
counter = 0

while counter <= 8:
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    db = client.sheetsDB
    currentTime = datetime.now()
    collection = db['printersindex'] # current db
    printersIndex = [156, 177, 162, 164, 223, 160, 153, 141, 196] # current values
    printersThreshold = []
    collection.insert_many([{'timestamp': currentTime, str(counter): printersIndex[counter]}]) # current values
    counter = counter + 1