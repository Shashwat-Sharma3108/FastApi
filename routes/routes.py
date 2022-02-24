import json

from fastapi import APIRouter
from config.database import collection
from models.model import Model
from schemas.schemas import multipleSerializer, serializer
from bson import ObjectId
router = APIRouter()

#getting data from database
@router.get("/getall")
def get():
    data = multipleSerializer(collection.find())
    return {"status" : "ok","data":data}

#getting single data from database
@router.get("/get/{id}")
def getOne(id: str):
    # print("reached")
    data = multipleSerializer(collection.find_one({"_id":ObjectId(id)}))
    # print("passed")
    # print(type(data))
    
    # data_str = str(data)
    # try:
    #     data_json = json.dumps(data_str)  
    #     print(data_json)

    # except Exception as e:
    #     print(str(e))
    return {"status" : "Ok" , "result" : data}

#posting to database
@router.post("/insert")
def posting(item : Model):
    _id = collection.insert_one(dict(item))
    insertedItem = multipleSerializer(collection.find({"_id":_id.inserted_id}))
    return {"status" : "Ok", "result" : insertedItem}

#updating
@router.put("/update/{id}")
def updating(id: str, item:Model):
    collection.find_one_and_update({"_id": ObjectId(id)},{
        "$set":dict(item)
    })
    updatedItem = collection.find({"id" : ObjectId(id)})
    return{"status" : "Ok" , "result" : updatedItem}

#Deleting
@router.delete("/delete/{id}")
def deleting(id : str):
    collection.find_one_and_delete({"_id" : ObjectId(id)})
    return{"status" : "Ok" , "result" : "Deleted!"}

#Bonus Queries

#1. Getting Discounted Items
@router.get("/count_discounted_products")
def discount():
    data = (collection.find(
        {"$expr": {"$lt": ["$offer_price_value", "$regular_price_value"]}}
    ).count())
    return{"status" : "Ok" , "result" : data}

#2. Unique Brand Names
@router.get("/list_unique_brands")
def distinctBrands():
    data = (collection.distinct("brand_name"))
    return{"status" : "Ok" , "result" : data}

#3.  How many products have offer price greater than 300?
@router.get("/count_high_offer_price")
def offerPrice():
    data = collection.find({"offer_price_value" : {"$gt":300}}).count()
    return{"status" : "Ok" , "result" : data}
