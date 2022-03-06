from models import Student
from db import session


def create_student():
    student = Student(name="Khushi", age=13, grade="8")
    session.add(student)
    # session.add_all([s1, s2])
    session.commit()


def get_student():
    # get all
    students = session.query(Student)
    print(students)
    for student in students:
        print(student.name)

    # get data in order
    students = session.query(Student).order_by(Student.name)
    for student in students:
        print(student.name)

    # get data by filtering
    # student = session.query(Student).filter(Student.name == 'Dhruv').first()
    student = session.query(Student).filter(Student.name == 'Dhruv').all()
    # print(str(student.statement))
    print(student)

    # Count of results

    student_count = session.query(Student).filter().count()
    print(student_count)


def update_student():
    student = session.query(Student).filter(Student.name == 'Khushi').first()
    student.grade = "Eighth"
    session.commit()

def delete_student():
    student = session.query(Student).filter(Student.name == 'Khushi').first()
    session.delete(student)
    session.commit()

#create_student
get_student()
# update_student()
# delete_student()