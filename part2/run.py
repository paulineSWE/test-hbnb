from flask import Flask
from flask_restx import Api
from app.api.v1 import users_ns, amenities_ns

app = Flask(__name__)
api = Api(app)

api.add_namespace(users_ns, path='/api/v1/users')
api.add_namespace(amenities_ns, path='/api/v1/amenities')

if __name__ == '__main__':
    app.run(debug=True)
