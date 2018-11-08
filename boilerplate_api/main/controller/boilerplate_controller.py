from flask_restplus import Namespace, Resource
from ..service.boilerplate_service import boilerplate_service

api = Namespace('boilerplate', description='boilerplate api to fill in with functionality')


@api.route('/')
class BoilerplateEndpoint(Resource):
    @api.doc('boilerplate endpoint')
    def get(self):
        return boilerplate_service()

