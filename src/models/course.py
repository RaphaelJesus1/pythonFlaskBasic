from . import db 

#configura modelo de dados do AUTHOR
class Course(db.Model):
    __tablename__ = 'course'

    course_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text())
    study_area = db.Column(db.Text())


    def __str__(self):
        return self.name

    def get_course_id(self):
        return self.course_id

  

