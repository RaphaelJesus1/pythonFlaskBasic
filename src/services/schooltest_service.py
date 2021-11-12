from src.models import db
from src.models.schooltest import SchoolTest
from src.config.restplus import  json_abort
from sqlalchemy.exc import SQLAlchemyError
import datetime

#importa a consulta de course e incluir um apelido ao get para evitar conflito com o get do student
from src.services.student_service import get as get_student

### SCHOOL TEST SERVICE
### gerenciar as regras de negocio e CRUD do SchoolTest
###

def create(data):
    try:

        title = data.get('title')
        if not title:
            json_abort(400,"Title is required")

        test_grade = data.get('test_grade')
        if not test_grade:
            json_abort(400,"Test_grade is required")

        concept = data.get('concept')
        if not concept:
            json_abort(400,"Concept is required")

        student_id = data.get('student_id')
        if not student_id:
            json_abort(400,"Student_id is required")

        student = get_student(student_id)
 
        created = datetime.datetime.now()

        schooltest = SchoolTest(title=title,test_grade=test_grade,concept=concept,created=created, student_id=student_id,student=student)
        db.session.add(schooltest)
        db.session.commit()

        return schooltest

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)

# Retorna todos os estudantes
def getSchoolTests():
    try:
        schooltest = SchoolTest.query.all()

        if not schooltest:
            json_abort(400,"School test not found")
        else:
            return schooltest

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)

# Busca pelo id e retorna com os dependentes
def get(id):
    try:
        schooltest = SchoolTest.query.filter_by(schooltest_id=id).first()

        if not schooltest:
            json_abort(400,"Student not found")

        return schooltest

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)

def change(id, data):
    try:
        
        schooltest = SchoolTest.query.filter_by(schooltest_id=id).first()

        if not schooltest:
            json_abort(400,"School test not found")
        else:

            title = data.get('title')
            if not title:
                json_abort(400,"Title is required")

            test_grade = data.get('test_grade')
            if not test_grade:
                json_abort(400,"Test_grade is required")

            concept = data.get('concept')
            if not concept:
                json_abort(400,"Concept is required")

            student_id = data.get('student_id')
            if not student_id:
                json_abort(400,"Student_id is required")
 
            db.session.query(SchoolTest)\
                .filter(SchoolTest.schooltest_id == id)\
                .update({
                    "title": title,
                    "test_grade": test_grade,
                    "concept": concept,
                })

            db.session.commit()
        
            return schooltest

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def delete(id):
    try:
        
        schooltest = SchoolTest.query.filter_by(schooltest_id=id).first()

        if not schooltest:
            json_abort(400,"School test not found")
        else:
            db.session.delete(schooltest)
            db.session.commit()
        
            return schooltest

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)