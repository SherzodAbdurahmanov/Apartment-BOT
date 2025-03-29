import os

from peewee import Model, SqliteDatabase, CharField, TextField, IntegerField

DB_PATH = os.path.join(os.path.dirname(__file__), "apartments.db")

db = SqliteDatabase(DB_PATH)


class Apartment(Model):
    owner_id = IntegerField()
    photo = CharField()
    city = CharField()
    address = TextField()
    description = TextField()
    price = IntegerField()
    contact = CharField()

    class Meta:
        database = db


db.connect()
db.create_tables([Apartment])
db.close()
