from pymongo import MongoClient, ASCENDING

collectionName = "BitcoinData"

client = MongoClient()
db = client.get_database('local')
collection = db.get_collection(collectionName)

items = collection.find()

with open("BitcoinData.csv","w") as f:
    for item in items:
        f.write(str(item['_id']['bar'])+","+str(item['volBTC'])+","+str(item['volUSD'])+","+str(item['maxPrice'])+","+str(item['minPrice'])+","+str(item['numberTrades'])+","+str(item['open'])+","+str(item['close'])+","+str(item['avgPrice'])+"/n")

f.close()