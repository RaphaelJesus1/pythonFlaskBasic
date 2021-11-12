from flask_restplus import fields
from src.config.restplus import api


schooltest_request = api.model('School test Request', {
    'title': fields.String(required=True, description='title school test'),
    'test_grade': fields.Float(required=True, description='test_grade school test'),
    'concept': fields.String(required=True, description='concept school test'),
    'student_id': fields.Integer(required=True, description='school test student ID ')
})

schooltest_result = api.model('School test Result', {
    'schooltest_id': fields.Integer(required=True, description='school test Id'),
    'title': fields.String(required=True, description='title school test'),
    'test_grade': fields.Float(required=True, description='test_grade school test'),
    'concept': fields.String(required=True, description='concept school test'),
    'student_id': fields.Integer(required=True, description='school test student ID '),
    'created': fields.DateTime(required=True, description='date school test created')
})
