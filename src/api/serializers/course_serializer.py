from flask_restplus import fields
from src.config.restplus import api
from .student_serializer import student_result


course_request = api.model('Course Request', {
    'name': fields.String(required=True, description='name course') ,
    'study_area': fields.String(required=True, description='text course'),
})

course_result = api.model('Course Result', {
    'course_id': fields.Integer(required=True, description='Course Id'),
    'name': fields.String(required=True, description='name course'), 
    'study_area': fields.String(required=True, description='text course'),
})
