# from flask import Flask, jsonify, request
from peewee import *
# from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('flash_cards', user='ari', password='12345',
                        host='localhost', port=5432)

db.connect()


class BaseModel(Model):
    class Meta:
        database = db


class Front(BaseModel):
    question: CharField()
    flipAround: CharField()


class Back(BaseModel):
    answer: CharField()


db.drop_tables([Front, Back])
db.create_tables([Front, Back])

firstQuestion = Front(question='Some question', flipAround='Yes')
firstQuestion.save()
