from flask_restplus import fields
from src.config.restplus import api
from .schooltest_serializer import schooltest_result


student_request = api.model('Student Request', {
    'course_id': fields.Integer(required=True, description='student course ID'),
    'name': fields.String(required=True, description='name student'),
    'age': fields.Integer(required=True, description='age student'),
    'cpf': fields.String(required=True, description='cpf student'),
})

student_result = api.model('Student Result', {
    'student_id': fields.Integer(required=True, description='student Id'),
    'course_id': fields.Integer(required=True, description='course Id'),
    'name': fields.String(required=True, description='name student'),
    'age': fields.String(required=True, description='age student'),
    'cpf': fields.String(required=True, description='cpf student'),
    'created': fields.DateTime(required=True, description='date student created')
})

student_schooltests_result = api.model('Student Result', {
    'student_id': fields.Integer(required=True, description='student Id'),
    'course_id': fields.Integer(required=True, description='course Id'),
    'name': fields.String(required=True, description='name student'),
    'age': fields.String(required=True, description='age student'),
    'cpf': fields.String(required=True, description='cpf student'),
    'created': fields.DateTime(required=True, description='date student created'),
    'schooltests': fields.List(fields.Nested(schooltest_result), required=True, description='list of school tests')
})
