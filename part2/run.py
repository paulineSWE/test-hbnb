from flask import Flask
from flask_restx import Api
from app.api.v1.users import users_bp

app = Flask(__name__)
api = Api(app, title='User API', version='1.0', description='A simple User API')

api.add_namespace(users_bp, path='/api/v1/users')

if __name__ == '__main__':
    app.run(debug=True)
