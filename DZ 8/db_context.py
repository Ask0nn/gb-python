from peewee import *


db = SqliteDatabase('../phones.db')


class BaseModel(Model):
    class Meta:
        database = db


class Contacts(BaseModel):
    id = AutoField(primary_key=True, column_name='id')
    name = TextField(null=False, column_name="name")
    phones = TextField(null=False, column_name="phones")


def init():
    db.close()
    db.connect()
    db.create_tables(Contacts)

