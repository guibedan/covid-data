from marshmallow import Schema, fields, validate


class AddCities(Schema):
    city = fields.String(required=True, validate=validate.Length(min=1, max=255))
    state = fields.String(required=True)
    city_ibge_code = fields.String(required=True)
    population = fields.Integer(required=True)
    cases = fields.Integer(required=True)
    deaths = fields.Integer(required=True)
    incidence = fields.Float(required=True)
    mortality = fields.Float(required=True)
