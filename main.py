import pymongo

DEFAULT_CONNECTION_URL = "mongodb://localhost:27017"
DB_NAME = "Assignment"
client = pymongo.MongoClient(DEFAULT_CONNECTION_URL)

database = client['DB_NAME']

record = {
    "Product": 'Oppo',
    "Name": 'Flipkart Customer',
    "Rating": '5',
    "Comment": 'Camera quality is best 👌 awesome luck charging and sound 100% good working'
    }

collection_name = "Flip_kart"
collection = database[collection_name]

collection.insert_one(record)

record = {
    "Product": 'Oppo',
    "Name": 'Ashis Mishra',
    "Rating": '5',
    "Comment": 'Good value for 5G product. Features are excellent and switching screens is very smooth. Screen display is awesome and so is the sound quality'

}
collection.insert_one(record)

list_of_records = [
    {
        "Product": 'Oppo',
        "Name": 'Haroon Rasheed',
        "Rating": '1',
        "Comment": 'Camera quality not good and battery performance not good and other wise phone to good',

    },
    {
        "Product": 'Oppo',
        "Name": 'Jignesh D Pathak',
        "Rating": '5',
        "Comment": 'Awesome Camera... Battery Clearity.....Nice phone.... In low budget',

    },
    {
        "Product": 'Oppo',
        "Name": 'mridul jha',
        "Rating": '4',
        "Comment": 'Best',

    }
]
collection.insert_many(list_of_records)

