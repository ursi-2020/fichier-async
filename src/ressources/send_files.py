from flask_restful import reqparse, Resource
from src.app_dic import add_app_to_dict


parser = reqparse.RequestParser()
parser.add_argument('app', type=str, required=True, help='Name of the app which you send the files')
parser.add_argument('path', type=str, required=True, help='the path of the files you want to send')


class Send(Resource):
    def post(self):
        args = parser.parse_args(strict=True)
        add_app_to_dict(args['app'], args['path'])

        return "successfully sent",  200