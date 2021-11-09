from flask_restplus import fields
from src.config.restplus import api


author_request = api.model('Author Request', {
    'first_name': fields.String(required=True, description='text post') ,
    'last_name': fields.String(required=True, description='text post'),
    'age': fields.Integer(required=True, description='post age'),
})

author_result = api.model('Author Result', {
    'id': fields.Integer(required=True, description='Post Id'),
    'first_name': fields.String(required=True, description='text post'), 
    'last_name': fields.String(required=True, description='text post'),
    'age': fields.Integer(required=True, description='post age'),
})
