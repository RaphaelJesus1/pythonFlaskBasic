from . import db
from .course import Course

#configura modelo de dados do POST
class Student(db.Model):
    __tablename__ = 'student'

    student_id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.Text())
    created = db.Column(db.DateTime)
    age = db.Column(db.Integer)
    cpf = db.Column(db.Text())
    course_id = db.Column(
        db.Integer, db.ForeignKey('course.course_id', ondelete='CASCADE'))
    course = db.relationship('Course')

    def __str__(self):
        return self.name

    def get_student_id(self):
        return self.student_id