import datetime
import os
import urllib.parse
from peewee import *

urllib.parse.uses_netloc.append('postgres')
url = urllib.parse.urlparse(os.environ.get('DATABASE_URL','postgres://localhost:5432/postgres'))

DATABASE = PostgresqlDatabase(
    url.path[1:],
    password= url.password,
    host= url.hostname,
    port= url.port
)

class Course(Model):
    title = CharField()
    url = CharField(unique=True)
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

class Review(Model):
    course = ForeignKeyField(Course,related_name='review_set')
    rating = IntegerField()
    comment = TextField(default='')
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Course,Review], safe=True)
    DATABASE.close()