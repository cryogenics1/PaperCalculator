from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymongo
from datetime import datetime

def main():
    pass

def concatenateURL(x):
    urlConcatenated = 'http://' + printers[x] + '/cgi-bin/dynamic/printer/config/reports/devicestatistics.html'
    return urlConcatenated

def scrapData():
    sheetsList = []
    counter = 0
    print("Scraping data...")
    while True: # loop to keep pulling data
         if counter <= 8: # always 8
            url = concatenateURL(counter)
            htmlPage = urlopen(url).read()
            soup = BeautifulSoup(htmlPage, features="html.parser")
            cleanPage = soup.getText()
            pageSplitter = cleanPage.split()
            sheetsList.insert(counter, pageSplitter[printersIndex[counter]]) # inserting a list with the data of the splitted page
            counter += 1

         elif counter >= 8: #always 8
            print("Adding to database...")
            sheetsList = list(map(int, sheetsList)) 
            print(*sheetsList) # just for monitoring :D
            print(*thresholdList)
            valueOne = sum(thresholdList)
            valueTwo = sum(sheetsList)
            finalSum = valueTwo - valueOne
            return finalSum
            break
         
def writeDB(x, y, z): # NOTE: x = value, y = field, z = collection, e.g: writeDB(2, 'Sheets', 'A4Sheets')
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    db = client.sheetsDB
    collection = db[z]
    currentTime = datetime.now()
    collection.insert_many([{'timestamp': currentTime, y: x}])
    print(f'Inserted: {x}, on {y}, in {z}')

printers = [
'192.168.0.90', '192.168.0.91', '192.168.0.92', '192.168.0.93',
'192.168.0.94', '192.168.0.95', '192.168.0.96', '192.168.0.97',
'192.168.0.98']

printersIndex = [156, 177, 162, 164, 223, 160, 153, 141, 196]

thresholdList = [239887, 522499, 114475, 163626, 526910, 484607, 43555, 131545, 294676] #294676 add as the last index
 # NOTE: this is hardcoded, you shouldn't leave like this, it's ugly.












# 90 = 156
# 91 = 177
# 92 = 162
# 93 = 164 
# 94 = 223
# 95 = 160
# 96 = 153
# 97 = 141
# 98 = 196
