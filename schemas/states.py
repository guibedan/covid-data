from marshmallow import Schema, fields, validate


class AddStates(Schema):
    name = fields.String(required=True, validate=validate.Length(min=1, max=255))
    cases = fields.Integer(required=True)
    deaths = fields.Integer(required=True)
    incidence = fields.Float(required=True)
    mortality = fields.Float(required=True)
