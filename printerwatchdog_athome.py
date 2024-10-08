from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymongo
from datetime import datetime
'''
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
 '''   
def scrapData():
    sheetsList = []
    counter = 0
    print("Scraping data...")
    while True: # loop to keep pulling data
        if counter >= 9: #always 9
            print("Adding to database...")
            
            
            # NOTE: The difference between this file and the other one, is that this one is for testing at home, without the printers connected on the local network.

            #sheetsList = list(map(int, sheetsList)) 
            thresholdList = [239887, 522499, 114475, 
                            163626, 526910, 484607, # NOTE: this is hardcoded, you shouldn't leave like this, it's ugly.
                            43555, 131545, 294676]
            sheetsList = [239887, 522499, 114475, 
                            163626, 526910, 484607, # NOTE: this is hardcoded, you shouldn't leave like this, it's ugly.
                            43555, 131545, 294776]
            
            print(*sheetsList) # just for monitoring :D
            print(*thresholdList)
            valueOne = sum(thresholdList)
            valueTwo = sum(sheetsList)
            finalSum = valueTwo - valueOne
            return finalSum
            break
        elif counter <= 9: # always 9
            #switchReturn = switch(counter)
            #url = concatenateURL(counter)
            #htmlPage = urlopen(url).read()
            #soup = BeautifulSoup(htmlPage, features="html.parser")
            #cleanPage = soup.getText()
            #pageSplitter = cleanPage.split()
            #sheetsList.insert(counter, pageSplitter[switchReturn]) 
            counter += 1

def writeDBFinalSum():
    finalSum = scrapData()
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    db = client.sheetsDB
    collection = db['A4Sheet']
    currentTime = datetime.now()
    collection.insert_many([{'timestamp': currentTime, 'Sheets': finalSum}])
    print(f'Inserted: %d' % finalSum)

def writeDB(x, y, z): # x = value, y = field, z = collection, e.g: writeDB(2, 'Sheets', 'A4Sheets')
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    db = client.sheetsDB
    collection = db[z]
    currentTime = datetime.now()
    collection.insert_many([{'timestamp': currentTime, y: x}])
    print(f'Inserted: {x}, on {y}, in {z}')
