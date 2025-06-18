from flask_restx import Namespace, Resource, fields
from flask import request
from app.services import facade

api = Namespace('amenities', description='Amenity operations')

# ----- MODELS -----

# Modèle d'entrée (input)
amenity_model = api.model('AmenityInput', {
    'name': fields.String(required=True, description='Name of the amenity')
})

# Modèle de sortie (output)
amenity_output_model = api.model('AmenityOutput', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Amenity name'),
    'created_at': fields.DateTime(description='Creation timestamp'),
    'updated_at': fields.DateTime(description='Last update timestamp')
})

# ----- ROUTES -----

@api.route('/')
class AmenityList(Resource):
    @api.expect(amenity_model)
    @api.marshal_with(amenity_output_model, code=201)
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new amenity"""
        data = request.json
        try:
            new_amenity = facade.create_amenity(data)
            return new_amenity.to_dict(), 201
        except ValueError as e:
            return {'error': str(e)}, 400

    @api.marshal_list_with(amenity_output_model)
    @api.response(200, 'List of amenities retrieved successfully')
    def get(self):
        """Retrieve a list of all amenities"""
        amenities = facade.get_all_amenities()
        return [a.to_dict() for a in amenities], 200


@api.route('/<string:amenity_id>')
class AmenityResource(Resource):
    @api.marshal_with(amenity_output_model)
    @api.response(200, 'Amenity details retrieved successfully')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """Get amenity details by ID"""
        amenity = facade.get_amenity(amenity_id)
        if amenity:
            return amenity.to_dict(), 200
        return {'error': 'Amenity not found'}, 404

    @api.expect(amenity_model)
    @api.marshal_with(amenity_output_model)
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input data')
    def put(self, amenity_id):
        """Update an amenity's information"""
        data = request.json
        updated = facade.update_amenity(amenity_id, data)
        if updated:
            return updated.to_dict(), 200
        return {'error': 'Amenity not found'}, 404
