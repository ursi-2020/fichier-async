from flask import Flask
from flask_restful import Resource, Api
from src.ressources.register import Register
from src.ressources.send_files import Send

app = Flask(__name__)
api = Api(app)

api.add_resource(Register)
api.add_resource(Send)


if __name__ == '__main__':
    app.run(debug=True)