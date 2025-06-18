from flask_restx import Api
from .users import api as users_ns
from .amenities import api as amenities_ns

# On instancie ici l'objet Api global
api = Api(
    title="HBnB API",
    version="1.0",
    description="API for managing users and amenities in the HBnB app"
)

# Enregistrement des namespaces
api.add_namespace(users_ns, path='/api/v1/users')
api.add_namespace(amenities_ns, path='/api/v1/amenities')
