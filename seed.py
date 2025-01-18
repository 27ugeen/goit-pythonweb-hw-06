from faker import Faker
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from models import Group, Teacher, Subject, Student, Grade, Base
import random
from datetime import datetime, timedelta

DATABASE_URL = "postgresql+psycopg2://postgres:mysecretpassword@localhost:5432/student_management"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)

fake = Faker()

NUM_GROUPS = 3
NUM_TEACHERS = 5
NUM_SUBJECTS = 7
NUM_STUDENTS = 30
NUM_GRADES = 100

def seed_data():
    with Session(engine) as session:
        groups = [Group(name=f"Group {i+1}") for i in range(NUM_GROUPS)]
        session.add_all(groups)
        session.commit()

        teachers = [Teacher(name=fake.name()) for _ in range(NUM_TEACHERS)]
        session.add_all(teachers)
        session.commit()

        subjects = [
            Subject(
                name=f"Mandatory Course {i+1}" if i == 0 else fake.job(),
                teacher_id=teachers[0].id if i == 0 else random.choice(teachers).id
            )
            for i in range(NUM_SUBJECTS)
        ]
        session.add_all(subjects)
        session.commit()

        students = [
            Student(
                name=fake.name(),
                group_id=random.choice(groups).id
            )
            for _ in range(NUM_STUDENTS)
        ]
        session.add_all(students)
        session.commit()

        grades = []
        for _ in range(NUM_GRADES):
            subject = random.choice(subjects)
            if subject.teacher_id == teachers[0].id:
                student = random.choice(students)
            else:
                student = random.choice(students)
            grades.append(
                Grade(
                    student_id=student.id,
                    subject_id=subject.id,
                    date=fake.date_between(start_date="-1y", end_date="today"),
                    grade=round(random.uniform(2, 5), 2)
                )
            )
        session.add_all(grades)
        session.commit()

if __name__ == "__main__":
    seed_data()
    print("Database seeded successfully!")