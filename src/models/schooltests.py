from . import db
from .student import Student

#configura modelo de dados do POST
class SchoolTests(db.Model):
    __tablename__ = 'schooltests'

    school_tests_id = db.Column(db.Integer, primary_key=True) 
    title = db.Column(db.Text())
    created = db.Column(db.DateTime)
    test_grade = db.Column(db.Float)
    concept = db.Column(db.Text())
    student_id = db.Column(
        db.Integer, db.ForeignKey('student.student_id', ondelete='CASCADE'))
    student = db.relationship('Student')

    def __str__(self):
        return self.title

    def get_school_tests_id(self):
        return self.school_tests_id