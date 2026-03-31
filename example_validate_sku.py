from db.validation_utils import SkuSchema
from marshmallow import ValidationError

sku_data = {
    "sku_code": "SKU123",
    "name": "Widget",
    "price": 19.99,
    "quantity": 100,
    "attributes": {"color": "red", "size": "M"}
}

schema = SkuSchema()
try:
    result = schema.load(sku_data)
    print("Valid SKU:", result)
except ValidationError as err:
    print("Validation errors:", err.messages)