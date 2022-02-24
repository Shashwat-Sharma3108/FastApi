def serializer(content)->dict:
    return{
        "id" : str(content["_id"]),
        "name": content["name"],
        "brand_name": content["brand_name"],
        "regular_price_value": content["regular_price_value"],
        "offer_price_value": content["offer_price_value"],
        "currency": content["currency"],
        "classification_l1" : content["classification_l1"],
        "classification_l2" : content["classification_l2"],
        "classification_l3" : content["classification_l3"],
        "classification_l4" : content["classification_l4"],
        "image_url" : content["image_url"]
    }

def multipleSerializer(contents) -> list:
    return [serializer(item) for item in contents]