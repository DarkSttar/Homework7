from random import randint, sample
from faker import Faker
import datetime
from connect_db import session
from models import Group, Student, Professor, Subject, Grade

NUMBER_STUDENTS = randint(30, 51)
NUMBER_GROUPS = 3
NUMBER_SUBJECTS = randint(5, 9)
NUMBER_PROFESSORS = randint(3, 6)
NUMBER_GRADES = randint(10, 20)

SUBJECTS = [
    "English",
    "Math",
    "Science",
    "History",
    "Social Studies",
    "Spanish",
    "French",
    "German",
    "Chinese",
    "Japanese",
    "Algebra",
    "Geometry",
    "Calculus",
    "Physics",
    "Chemistry",
    "Biology",
    "Geography",
    "Government",
    "Economics",
    "Psychology",
    "Sociology",
    "Art",
    "Music",
    "Theater",
    "Dance",
    "Literature",
    "Business",
    "Computer Science",
    "Engineering",
    "Helth",
    "Home economics",
    "Physical Education",
]

GROUP_NAME = ["A", "B", "C", "D", "E", "F"]


def generate_fake_data(
    num_students=30,
    num_groups=3,
    num_subjects=5,
    num_professors=3,
    num_grades=NUMBER_GRADES,
    subjects=SUBJECTS,
    group_name=GROUP_NAME,
) -> tuple:
    fake_data = Faker()
    fake_students = []
    fake_professors = []
    fake_subjects = []
    fake_groups = []

    fake_groups = sample(group_name, num_groups)

    fake_subjects = sample(subjects, num_subjects)

    for _ in range(num_students):
        fake_students.append(fake_data.name())

    for _ in range(num_professors):
        fake_professors.append(fake_data.name())

    for_groups = []
    group_id = 1
    for group in fake_groups:
        for_groups.append(Group(name=group, id=group_id))
        group_id += 1

    for_students = []
    student_id = 1
    for student in fake_students:
        for_students.append(
            Student(name=student, group_id=randint(1, num_groups), id=student_id)
        )
        student_id += 1

    for_subjects = []
    subject_id = 1
    for subject in fake_subjects:
        for_subjects.append(
            Subject(
                name=subject, professor_id=randint(1, num_professors), id=subject_id
            )
        )
        subject_id += 1

    for_professors = []
    professor_id = 1
    for professor in fake_professors:
        for_professors.append(Professor(name=professor, id=professor_id))
        professor_id += 1

    for_grades = []
    grades_id = 1
    for subject in for_subjects:
        for student in for_students:
            for g in range(NUMBER_GRADES):
                for_grades.append(
                    Grade(
                        grade=randint(1, 5),
                        date_grading=datetime.datetime(
                            2024, randint(1, 12), randint(1, 29)
                        ).date(),
                        student_id=student.id,
                        subject_id=subject.id,
                        id=grades_id,
                    )
                )
                grades_id += 1
                data = (
                    for_groups
                    + for_students
                    + for_professors
                    + for_subjects
                    + for_grades
                )
    return data


data = generate_fake_data()


if __name__ == "__main__":
    session.add_all(data)
    session.commit()
