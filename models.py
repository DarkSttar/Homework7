from datetime import datetime

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.sql.sqltypes import DateTime

__tablename__ = None

Base = declarative_base()

# Table Groups


class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(10), nullable=False)
    students = relationship("Student", cascade=("delete"), backref="groups")


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(60), nullable=False)
    group_id = Column(
        Integer, ForeignKey(Group.id, ondelete="SET NULL", onupdate="CASCADE")
    )


class Professor(Base):
    __tablename__ = "professors"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(60), nullable=False)
    subjects = relationship("Subject", backref="professors")


class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    professor_id = Column(
        Integer, ForeignKey(Professor.id, ondelete="CASCADE", onupdate="CASCADE")
    )
    grades = relationship("Grade", backref="subjects")


class Grade(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True, autoincrement=True)
    grade = Column(Float, nullable=False)
    date_grading = Column(DateTime)
    student_id = Column(
        Integer, ForeignKey(Student.id, ondelete="CASCADE", onupdate="CASCADE")
    )
    subject_id = Column(
        Integer, ForeignKey(Subject.id, ondelete="CASCADE", onupdate="CASCADE")
    )
