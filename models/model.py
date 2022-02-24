from pydantic import BaseModel

class Model(BaseModel):
    name: str
    brand_name: str
    regular_price_value: int
    offer_price_value: int
    currency: str
    classification_l1 : str
    classification_l2 : str
    classification_l3 : str
    classification_l4 : str
    image_url : str