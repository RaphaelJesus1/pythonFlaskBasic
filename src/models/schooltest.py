from . import db
from .student import Student

#configura modelo de dados do POST
class SchoolTest(db.Model):
    __tablename__ = 'schooltest'

    schooltest_id = db.Column(db.Integer, primary_key=True) 
    title = db.Column(db.Text())
    test_grade = db.Column(db.Float)
    concept = db.Column(db.Text())
    created = db.Column(db.DateTime)
    student_id = db.Column(
        db.Integer, db.ForeignKey('student.student_id', ondelete='CASCADE'))
    student = db.relationship('Student')

    def __str__(self):
        return self.title

    def get_schooltest_id(self):
        return self.schooltest_id