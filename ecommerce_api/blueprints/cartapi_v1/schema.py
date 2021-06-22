from marshmallow import Schema, fields, validate


def parse_payload(request):
    try:
        schema = ProductsCartSchema()
        return True, schema.load(request.get_json())
    except Exception as exc:
        return False, exc


class ProductSchema(Schema):

    id = fields.Integer(required=True, validate=validate.Range(min=1))
    quantity = fields.Integer(required=True, validate=validate.Range(min=1))


class ProductsCartSchema(Schema):

    products = fields.List(fields.Nested(ProductSchema), validate=validate.Length(min=1))
