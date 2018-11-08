from flask import Blueprint
from flask_restplus import Api

from .main.controller.boilerplate_controller import api as orch_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Flask Boilerplate API',
          version='1.0',
          description='Api to fill in with desired functionality')

api.add_namespace(orch_ns, path='/boilerplate')
