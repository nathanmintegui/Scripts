import pymongo

# MongoDB connection settings
mongo_uri = "mongodb://USERNAME:PASSWORD@HOST/DATABASE?ssl=true&connectTimeoutMS=5000&maxPoolSize=50"  
database_name = "database"  
collection_name = "collection"  

data_to_insert = [
    {
        "name": "John Doe",
        "email": "john@example.com",
        "age": 30,
    },
    {
        "name": "Jane Smith",
        "email": "jane@example.com",
        "age": 25,
    },
]

def insert_data():
    try:
        # Connect to MongoDB
        client = pymongo.MongoClient(mongo_uri)
        db = client[database_name]
        collection = db[collection_name]

        # Insert data into the collection
        result = collection.insert_many(data_to_insert)

        # Print the inserted document IDs
        print("Inserted document IDs:", result.inserted_ids)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    insert_data()

