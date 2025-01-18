from sqlalchemy.orm import Session
from db import engine
from my_select import *

with Session(engine) as session:
    print("Top 5 students by average grade:", select_1(session))
    print("Best student in subject 1:", select_2(session, 1))
    print("Average grade by group for subject 1:", select_3(session, 1))
    print("Average grade on the stream:", select_4(session))
    print("Courses taught by teacher 1:", select_5(session, 1))
    print("Students in group 1:", select_6(session, 1))
    print("Grades in group 1 for subject 1:", select_7(session, 1, 1))
    print("Average grade by teacher 1:", select_8(session, 1))
    print("Courses attended by student 2:", select_9(session, 2))
    print("Courses student 2 has with teacher 1:", select_10(session, 2, 1))