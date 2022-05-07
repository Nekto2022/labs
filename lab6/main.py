import cherrypy
from jinja2 import Environment, FileSystemLoader
from model import db, Student, init_db, Characteristic

env = Environment(loader=FileSystemLoader("templates"))


class Root(object):
    @cherrypy.expose
    def index(self):
        db.connect()
        students = []
        for student in Student.select().dicts():
            student['characteristic'] = Characteristic.get(id=student['characteristic_id']).goods
            students.append(student)
        db.close()
        template = env.get_template("index.html")
        return template.render({'students': students})

    @cherrypy.expose
    def create(self, n, name, email, group, good):
        db.connect()
        characteristic = Characteristic(goods=good)
        student = Student(n=n, name=name, email=email, group=group, characteristic_id=characteristic)
        characteristic.save()
        student.save()
        db.close()
        raise cherrypy.HTTPRedirect("/")

    @cherrypy.expose
    def update(self, id, n=None, name=None, email=None, group=None, good=None):
        db.connect()
        student = Student.select().where(Student.id==id).first()
        if n: student.n = n
        if name: student.name = name
        if email: student.email = email
        if group: student.group=group
        if good:
            c = Characteristic.get(id=student.characteristic_id)
            c.goods = good
            c.save()
        student.save()
        db.close()
        raise cherrypy.HTTPRedirect("/")

    @cherrypy.expose
    def delete(self, id):
        db.connect()
        Student.delete_by_id(Student.select().where(Student.id == id))
        db.close()
        raise cherrypy.HTTPRedirect("/")

    @cherrypy.expose
    def init_database(self):
        init_db()
        raise cherrypy.HTTPRedirect("/")


if __name__ == '__main__':
    cherrypy.quickstart(Root(), "/")
