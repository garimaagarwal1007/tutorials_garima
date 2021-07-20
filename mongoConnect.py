from pymongo import MongoClient


def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    # mongodb://127.0.0.1: 27017/?compressors=disabled&gssapiServiceName=mongodb
    CONNECTION_STRING = "mongodb+srv://<username>:<password>@<cluster-name>.mongodb.net/myFirstDatabase"
    conn_str = "mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb"

    client = MongoClient(conn_str)
    db_name = client["blogs"]
    collection_name = db_name["blog"]
    # find all items
    # all_item_details = collection_name.find()
    # for item in all_item_details:
    #     # This does not give a very readable output
    #     print(item)
    # # find item with author Richard
    # filter_query = {"auth_name":"Richard"}
    # filtered_item_details = collection_name.find(filter_query)
    # for item in filtered_item_details:
    #     print(item)

    # insert
    to_insert = [{'auth_name': 'Garima',
                  'blogs': [{'PostID': 'aI1se', 'likes': 45.0, 'dislikes': 41.0},
                            {'PostID': 'KLi1e', 'likes': 121.0, 'dislikes': 1.0},
                            {'PostID': 'v33l1', 'likes': 146.0, 'dislikes': 58.0},
                            {'PostID': 'a1Sl3', 'likes': 145.0, 'dislikes': 19.0}]},
                 {'auth_name': 'Akshay',
                  'blogs': [{'PostID': 'aI1se', 'likes': 45.0, 'dislikes': 41.0},
                            {'PostID': 'KLi1e', 'likes': 121.0, 'dislikes': 1.0},
                            {'PostID': 'v33l1', 'likes': 146.0, 'dislikes': 58.0},
                            {'PostID': 'a1Sl3', 'likes': 145.0, 'dislikes': 19.0}]},
                 {'auth_name': 'Damodar',
                  'blogs': [{'PostID': 'aI1se', 'likes': 45.0, 'dislikes': 41.0},
                            {'PostID': 'KLi1e', 'likes': 121.0, 'dislikes': 1.0},
                            {'PostID': 'v33l1', 'likes': 146.0, 'dislikes': 58.0},
                            {'PostID': 'a1Sl3', 'likes': 145.0, 'dislikes': 19.0}]}
                 ]
    #collection_name.insert_many(to_insert)
    # filter_query = {"auth_name": {"$in": ["Garima", "Akshay", "Damodar"]}}
    # filtered_item_details = collection_name.find(filter_query)
    # for item in filtered_item_details:
    #     print(item)

    # read nested records
    #test_
    test = [{"$unwind":"$blogs"},{"$match": {"blogs.likes" : {"$gt":500}}}]
    try:
        test_results = collection_name.aggregate(test)
    except Exception as e:
        print(e)
        exit()
    for item in test_results:
        print(item)

    # update
    # update_criteria = {"auth_name": "Garima"}
    # update_query = {"$set": {"auth_name": "SuperSmartGArima"}}
    # collection_name.update_many(update_criteria, update_query)


# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":
    # Get the database
    dbname = get_database()
