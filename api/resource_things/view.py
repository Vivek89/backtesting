from flask import Blueprint
from flask_restplus import Api, Resource


resource_things = Blueprint('resource_things', __name__)
api = Api(app=resource_things, doc='/docs')


@api.route('/resources')
class ResourceThings(Resource):

    def get(self):
        return 'Get Resource List'

    def post(self):
        return 'POST Resource List'
