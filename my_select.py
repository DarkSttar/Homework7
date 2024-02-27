from models import Group,Student,Professor,Subject,Grade
from sqlalchemy import func,and_
from connect_db import session


def query_1(session=session,limit=5):
    query = (session.query(Student.id.label('StudentID'),Student.name,func.avg(Grade.grade))
        .join(Grade,Grade.student_id == Student.id)
        .group_by(Student.id,Student.name)
        .order_by(func.avg(Grade.grade).desc())
        .limit(limit)
        .all())
    return query
    

def query_2(session=session,subjectID=1,limit=1):
    query = (session.query(Student.id.label('StudentID'),Student.name,Subject.name,func.avg(Grade.grade)) 
            .join(Student,Student.id == Grade.student_id)
            .join(Subject,and_(Subject.id == Grade.subject_id, Subject.id == subjectID))
            .group_by(Student.id,Subject.name)
            .order_by(func.avg(Grade.grade).desc())
            .limit(limit)
            .all())
    return query       
            

def query_3(session=session,subjectID=1):
    query = (session.query(Group.name.label('GroupName'),Subject.name.label('SubjectName'),func.avg(Grade.grade))
             .join(Student,Student.group_id == Group.id)
             .join(Grade,Grade.student_id == Student.id)
             .join(Subject,and_(Subject.id == Grade.subject_id , Subject.id == subjectID))
             .group_by('GroupName','SubjectName')
             .all()
             )
    return query



def query_4(session=session):
    query = (session.query(func.avg(Grade.grade))
          .all())
    return query


def query_5(session=session,professorID=1):
    query = (session.query(Professor.name,Subject.name)
             .join(Subject,Subject.professor_id == Professor.id)
             .where(Professor.id == professorID)
             .all())
    return query


def query_6(session=session,groupID=1):
    query = (session.query(Student.id,Student.name,Group.name)
            .join(Student,Student.group_id == Group.id)
            .where(Group.id == groupID)
            .all())
    return query



def query_7(session=session,groupID=1,subjectID=1):
    query = (session.query(Subject.name, Group.name,Student.id,Student.name,Grade.grade)
             .join(Student,Student.group_id == Group.id)
             .join(Grade,Grade.student_id == Student.id)
             .join(Subject, and_(Subject.id == Grade.subject_id, Subject.id == subjectID))
             .where(Group.id == groupID)
             .all())
    
    return query



def query_8(session=session,professorID=1):
    query = (session.query(Professor.id,Professor.name,Subject.name,func.avg(Grade.grade))
             .join(Subject,Subject.professor_id == Professor.id)
             .join(Grade,Grade.subject_id == Subject.id)
             .where(Professor.id == professorID)
             .group_by(Professor.id,Professor.name,Subject.name)
             .all())
    return query



def query_9(session=session,studentID=1):
    query = (session.query(Student.id,Student.name,Subject.name)
             .join(Grade,Grade.student_id == Student.id)
             .join(Subject,Subject.id == Grade.subject_id)
             .where(Student.id == studentID)
             .group_by(Subject.id,Student.id)
             .all())

    return query


def query_10(session=session,professorID=1,studentID=1):
    query = (session.query(Student.id,Student.name,Professor.name,Subject.name)
             .join(Grade,Grade.student_id == Student.id)
             .join(Subject,Subject.id == Grade.subject_id)
             .join(Professor,and_(Professor.id == Subject.professor_id,Professor.id == professorID))
             .where(Student.id == studentID)
             .group_by(Student.id,Professor.name,Subject.name)
             .all())
    return query
    














