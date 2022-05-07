from peewee import *

db = SqliteDatabase('student.db')


class Characteristic(Model):
    goods = CharField()

    class Meta:
        database = db


class Student(Model):
    n = IntegerField()
    name = CharField()
    email = CharField()
    group = CharField()
    characteristic_id = ForeignKeyField(Characteristic)

    class Meta:
        database = db


def init_db():
    with db:
        db.create_tables([Student, Characteristic])