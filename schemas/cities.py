from marshmallow import Schema, fields, validate


class AddCities(Schema):
    name = fields.String(required=True, validate=validate.Length(min=1, max=255))
    state_id = fields.UUID(required=True)
    cases = fields.Integer(required=True)
    deaths = fields.Integer(required=True)
    type_region = fields.String(required=True, validate=validate.Length(min=1, max=50))
