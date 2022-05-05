from peewee import *

db = SqliteDatabase('student.db')


class Good(Model):
    good = BooleanField()

    class Meta:
        database = db


class Student(Model):
    n = IntegerField()
    name = CharField()
    email = CharField()
    group = CharField()
    good_id = ForeignKeyField(Good)

    class Meta:
        database = db


def init_db():
    with db:
        db.create_tables([Student, Good])