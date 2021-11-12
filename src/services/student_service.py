from src.models import db
from src.models.student import Student
from src.models.schooltests import SchoolTests
from src.config.restplus import  json_abort
from sqlalchemy.exc import SQLAlchemyError
import datetime

#importa a consulta de course e incluir um apelido ao get para evitar conflito com o get do student
from src.services.course_service import get as get_course

### STUDENT SERVICE
### gerenciar as regras de negocio e CRUD do Student
###

def create(data):
    try:

        name = data.get('name')
        if not name:
            json_abort(400,"Name is required")

        age = data.get('age')
        if not age:
            json_abort(400,"Age is required")

        cpf = data.get('cpf')
        if not cpf:
            json_abort(400,"CPF is required")

        course_id = data.get('course_id')
        if not course_id:
            json_abort(400,"Course_id is required")

        course = get_course(course_id)
 
        created = datetime.datetime.now()

        student = Student(name=name,age=age,cpf=cpf,created=created, course_id=course_id,course=course)
        db.session.add(student)
        db.session.commit()

        return student

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)

# Retorna todos os estudantes
def getStudents():
    try:
        students = Student.query.all()

        if not students:
            json_abort(400,"Students not found")
        else:
            return students

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)

# Busca pelo id e retorna com os dependentes
def get(id):
    try:
        student = Student.query.filter_by(student_id=id).first()

        school_tests = SchoolTests.query.filter_by(student_id=id)

        if not student:
            json_abort(400,"Student not found")

        return student

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)

def change(id, data):
    try:
        
        student = Student.query.filter_by(student_id=id).first()

        if not student:
            json_abort(400,"Student not found")
        else:

            name = data.get('name')
            if not name:
                json_abort(400,"Name is required")

            age = data.get('age')
            if not age:
                json_abort(400,"Age is required")

            cpf = data.get('cpf')
            if not cpf:
                json_abort(400,"Cpf is required")
 
            db.session.query(Student)\
                .filter(Student.student_id == id)\
                .update({
                    "name": name,
                    "age": age,
                    "cpf": cpf
                })

            db.session.commit()
        
            return student

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def delete(id):
    try:
        
        student = Student.query.filter_by(student_id=id).first()

        if not student:
            json_abort(400,"Student not found")
        else:
            db.session.delete(student)
            db.session.commit()
        
            return student

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)