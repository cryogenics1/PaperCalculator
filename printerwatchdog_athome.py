from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymongo
from datetime import datetime

printers = [
'192.168.0.90', '192.168.0.91', '192.168.0.92', '192.168.0.93',
'192.168.0.94', '192.168.0.95', '192.168.0.96', '192.168.0.97',
'192.168.0.98']

def main():
    pass

def concatenateURL(x):
    urlConcatenated = 'http://' + printers[x] + '/cgi-bin/dynamic/printer/config/reports/devicestatistics.html'
    return urlConcatenated

def switch(printerSwitch): # gets all printers data based on the index
    if printerSwitch == 0:
        return 156
    elif printerSwitch == 1:
        return 177
    elif printerSwitch == 2:
        return 162
    elif printerSwitch == 3: 
        return 164
    elif printerSwitch == 4:
        return 223
    elif printerSwitch == 5:
        return 160
    elif printerSwitch == 6:
        return 153
    elif printerSwitch == 7:
        return 141
    elif printerSwitch == 8:
        return 196
    
def scrapData():
    sheetsList = []
    counter = 0
    print("Scraping data...")
    while True: # loop to keep pulling data
        if counter >= 8: #always 9
            print("Adding to database...")
            sheetsList = list(map(int, sheetsList)) # when the loop reaches the end, transforms all list into integer
            thresholdList = [239887, 522499, 114475, 
                            163626, 526910, 484607, # NOTE: this is hardcoded, you shouldn't leave like this, it's ugly.
                            43555, 131545] #294676 add as the last index
            #print(*sheetsList) # just for monitoring :D
            #print(*thresholdList)
            valueOne = sum(thresholdList)
            valueTwo = sum(sheetsList)
            finalSum = valueTwo - valueOne
            return finalSum
            break
        elif counter <= 8: # always 9
            switchReturn = switch(counter)
            url = concatenateURL(counter)
            htmlPage = urlopen(url).read()
            soup = BeautifulSoup(htmlPage, features="html.parser")
            cleanPage = soup.getText()
            pageSplitter = cleanPage.split()
            sheetsList.insert(counter, pageSplitter[switchReturn]) # inserting a list with the data of the splitted page
            counter += 1

def writeDBFinalSum():
    finalSum = scrapData()
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    db = client.sheetsDB
    collection = db['A4Sheet']
    currentTime = datetime.now()
    collection.insert_many([{'timestamp': currentTime, 'Sheets': finalSum}])
    print(f'Inserted: %d' % finalSum)

def writeDB(x, y, z): # NOTE: x = value, y = field, z = collection, e.g: writeDB(2, 'Sheets', 'A4Sheets')
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    db = client.sheetsDB
    collection = db[z]
    currentTime = datetime.now()
    collection.insert_many([{'timestamp': currentTime, y: x}])
    print(f'Inserted: {x}, on {y}, in {z}')
# 90 = 156
# 91 = 177
# 92 = 162
# 93 = 164 
# 94 = 223
# 95 = 160
# 96 = 153
# 97 = 141
# 98 = 196