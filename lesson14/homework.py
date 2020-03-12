"""Описать таблицы из lesson12/homework.sql при помощи sqlalchemy"""
from sqlalchemy import create_engine, MetaData, Column, Integer, String, Sequence, Index, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgres://postgres:1234@localhost:5432/postgres')
metadata = MetaData()

Base = declarative_base()


class Users(Base):
    ___tablename___ = 'app_users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String, nullable=False)

    __table_args__ = (Index('users_id_index', 'username', unique=True))

    def __init__(self, id, username):
        self.id = id
        self.username = username

    def __repr__(self):
        return '<app_users("%s")>' % (self.username)


class Tests(Base):
    __tablename__ = 'tests'
    id = Column(Integer, Sequence('test_id_seq'), primary_key=True)
    number = Column(Integer, nullable=False)
    text = Column(Integer, nullable=False)

    def __init__(self, id, number, text):
        self.id = id
        self.number = number
        self.text = text

    def __repr__(self):
        return '<tests("%s", "%s")>' % (self.number, self.text)


class Tests_Questions(Base):
    __tablename__ = 'tests_questions'
    id = Column(Integer, Sequence('tests_id_seq'), )
    test_id = Column(Integer, ForeignKey('tests.id'))
    question_id = Column(Integer, ForeignKey('Questions.id'))

    def __init__(self, id, test_id, question_id):
        self.id = id
        self.test_id = test_id
        self.question_id = question_id

    def __repr__(self):
        return '<tests_questions("%s", "%s")>' % (self.test_id, self.question_id)


class Questions(Base):
    __tablename__ = 'questions'
    id = Column(Integer, Sequence('question_id_seq'), primary_key=True)
    number = Column(Integer)
    text = Column(String)

    def __init__(self, id, number, text):
        self.id = id
        self.number = number
        self.text = text

    def __repr__(self):
        return '<questions("%s", "%s")>' % (self.number, self.text)


class Answers(Base):
    __tablename__ = 'answers'
    id = Column(Integer, Sequence('answer_id_seq'), primary_key=True, nullable=False)
    text = Column(String, nullable=False)
    is_correct = Column(bool)
    question_id = (Integer, ForeignKey('questions.id'))

    def __init__(self, id, text, is_correct, question_id):
        self.id = id
        self.text = text
        self.is_correct = is_correct
        self.question_id = question_id

    def __repr__(self):
        return '<answers("%s", "%s", "%s")>' % (self.text, self.is_correct, self.question_id)


class Users_answers(Base):
    __tablename__ = 'users_answer'
    id = Column(Integer, Sequence('users_answer_id_seq'), primary_key=True)
    tests_questions_id = Column(Integer, ForeignKey('tests_questions.id'))
    user_id = Column(Integer, ForeignKey('app_users.id'))
    answer_id = Column(Integer, ForeignKey('answers.id'))

    __table_args__ = Index('users_answers', 'user_id', 'tests_questions_id', unique=True)

    def __init__(self, id, tests_question_id, user_id, answer_id):
        self.id = id
        self.tests_questions_id = tests_question_id
        self.user_id = user_id
        self.answer_id = answer_id

    def __repr__(self):
        return '<users_answer("%s", "%s", "%s")>' % (self.tests_questions_id, self.user_id, self.answer_id)
