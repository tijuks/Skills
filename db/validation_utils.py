from marshmallow import Schema, fields, validate, ValidationError

class SkuSchema(Schema):
    sku_code = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    price = fields.Float(required=True)
    quantity = fields.Integer(required=True, validate=validate.Range(min=0))
    attributes = fields.Dict()

# Example usage:
# try:
#     data = SkuSchema().load(request.json)
# except ValidationError as err:
#     print(err.messages)