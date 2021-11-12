from src.models import db
from src.models.course import Course
from src.models.student import Student
from src.config.restplus import  json_abort
from sqlalchemy.exc import SQLAlchemyError 

### COURSE SERVICE
### gerenciar as regras de negocio e CRUD do course
###

# Cria um novo registro
def create(data):
    try:

        name = data.get('name')
        if not name:
            json_abort(400,"Name is required")

        study_area = data.get('study_area')
        if not study_area:
            json_abort(400,"Study Area is required")

 
        course = Course(name=name,study_area=study_area)
        db.session.add(course)
        db.session.commit()

        return course

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)

# Retorna todos os cursos
def getCourses():
    try:
        courses = Course.query.all()

        if not courses:
            json_abort(400,"Courses not found")
        else:
            return courses

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


# Busca pelo id e retorna com os dependentes
def get(id):
    try:
        course = Course.query.filter_by(course_id=id).first()

        students = Student.query.filter_by(course_id=id)

        if not course:
            json_abort(400,"Course not found")
        
        course.students = students    
        return course

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)

# Atualiza baseado no id
def change(id, data):
    try:
        
        course = Course.query.filter_by(course_id=id).first()

        if not course:
            json_abort(400,"Course not found")
        else:

            name = data.get('name')
            if not name:
                json_abort(400,"Name is required")

            study_area = data.get('study_area')
            if not study_area:
                json_abort(400,"Study Area is required")

            
            db.session.query(Course)\
                .filter(Course.course_id == id)\
                .update({
                    "name": name,
                    "study_area": study_area
                })
            
            db.session.commit()
        
            return course

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)

# Deleta um objeto baseado no id
def delete(id):
    try:
        
        course = Course.query.filter_by(course_id=id).first()

        if not course:
            json_abort(400,"Course not found")
        else:
            db.session.delete(course)
            db.session.commit()
        
            return course

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)