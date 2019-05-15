from flask import Blueprint
from flask_restplus import Api, Resource


second_things = Blueprint('second_things', __name__)
api = Api(app=second_things, doc='/docs')


@api.route('/second')
class SecondThings(Resource):

    def get(self):
        return 'Get Resource List'

    def post(self):
        return 'POST Resource List'
