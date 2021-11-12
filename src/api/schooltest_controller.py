from flask import request
from flask_restplus import Resource
from src.config.restplus import api
from src.api.serializers.schooltest_serializer import schooltest_request, schooltest_result
from src.services.schooltest_service import create, change, delete, get, getSchoolTests
 

ns = api.namespace('api/schooltest', description='Operations related to schooltests')


@ns.route('')#refine rota
class SchoolTestCollection(Resource):
    @api.expect(schooltest_request)#define parametro de entrada para a documentaçao do swagger
    @api.marshal_with(schooltest_result)#define resultado da metodo 
    def post(self):
        """
        Create a new schooltest
        """ 
        schooltest = create(request.json)
        return schooltest
    
    @api.marshal_with(schooltest_result)
    def get(self):
        """
        Get schooltests
        """ 
        schooltests = getSchoolTests()
        return schooltests

 

@ns.route('/<int:id>')
class SchoolTestIDCollection(Resource): 
    @api.marshal_with(schooltest_result)
    def get(self, id):
        """
        Get schooltest by ID
        """ 
        schooltest = get(id)
        return schooltest 


    @api.expect(schooltest_request)
    @api.marshal_with(schooltest_result)
    def put(self, id):
        """
        Change schooltest by ID
        """ 
        schooltest = change(id,request.json)
        return schooltest 
 
    @api.marshal_with(schooltest_result)
    def delete(self, id):
        """
        Delete schooltest by ID
        """ 
        schooltest = delete(id)
        return schooltest