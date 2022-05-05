import cherrypy
from jinja2 import Environment, FileSystemLoader
from model import db, Student, init_db

env = Environment(loader=FileSystemLoader("templates"))


class Root(object):
    @cherrypy.expose
    def index(self):
        db.connect()
        students = [student for student in Student.select().dicts()]
        db.close()
        template = env.get_template("index.html")
        return template.render({'students': students})

    @cherrypy.expose
    def create(self, n, name, email, group):
        db.connect()
        student = Student(n=n, name=name, email=email, group=group)
        student.save()
        db.close()
        return "successs"

    @cherrypy.expose
    def update(self, id, n=None, name=None, email=None, group=None):
        db.connect()
        student = Student.select().where(Student.id==id).first()
        if n: student.n = n
        if name: student.name = name
        if email: student.email = email
        if group: student.group=group
        student.save()
        db.close()
        return "success"

    @cherrypy.expose
    def delete(self, id):
        db.connect()
        Student.delete_by_id(Student.select().where(Student.id == id))
        db.close()
        return "success"


if __name__ == '__main__':
    cherrypy.quickstart(Root(), "/")
