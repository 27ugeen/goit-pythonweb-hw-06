from sqlalchemy.orm import Session
from models import Student, Group, Teacher, Subject, Grade
from sqlalchemy import func

def select_1(session: Session):
    """Знайти 5 студентів із найбільшим середнім балом з усіх предметів."""
    result = session.query(
        Student.name,
        func.avg(Grade.grade).label('average_grade')
    ).join(Grade).group_by(Student.id).order_by(func.avg(Grade.grade).desc()).limit(5).all()
    return result

def select_2(session: Session, subject_id: int):
    """Знайти студента із найвищим середнім балом з певного предмета."""
    result = session.query(
        Student.name,
        func.avg(Grade.grade).label('average_grade')
    ).join(Grade).filter(Grade.subject_id == subject_id).group_by(Student.id).order_by(func.avg(Grade.grade).desc()).first()
    return result

def select_3(session: Session, subject_id: int):
    """Знайти середній бал у групах з певного предмета."""
    result = session.query(
        Group.name,
        func.avg(Grade.grade).label('average_grade')
    ).select_from(Grade).join(Student, Grade.student_id == Student.id).join(Group, Student.group_id == Group.id).filter(Grade.subject_id == subject_id).group_by(Group.id).all()
    return result

def select_4(session: Session):
    """Знайти середній бал на потоці (по всій таблиці оцінок)."""
    result = session.query(func.avg(Grade.grade).label('average_grade')).scalar()
    return result

def select_5(session: Session, teacher_id: int):
    """Знайти які курси читає певний викладач."""
    result = session.query(Subject.name).filter(Subject.teacher_id == teacher_id).all()
    return result

def select_6(session: Session, group_id: int):
    """Знайти список студентів у певній групі."""
    result = session.query(Student.name).filter(Student.group_id == group_id).all()
    return result

def select_7(session: Session, group_id: int, subject_id: int):
    """Знайти оцінки студентів у окремій групі з певного предмета."""
    result = session.query(
        Student.name,
        Grade.grade
    ).join(Grade).filter(Student.group_id == group_id, Grade.subject_id == subject_id).all()
    return result

def select_8(session: Session, teacher_id: int):
    """Знайти середній бал, який ставить певний викладач зі своїх предметів."""
    result = session.query(
        func.avg(Grade.grade).label('average_grade')
    ).join(Subject).filter(Subject.teacher_id == teacher_id).scalar()
    return result

def select_9(session: Session, student_id: int):
    """Знайти список курсів, які відвідує певний студент."""
    result = session.query(Subject.name).join(Grade).filter(Grade.student_id == student_id).group_by(Subject.id).all()
    return result

def select_10(session: Session, student_id: int, teacher_id: int):
    """Список курсів, які певному студенту читає певний викладач."""
    result = session.query(Subject.name).join(Grade).filter(
        Grade.student_id == student_id,
        Subject.teacher_id == teacher_id
    ).group_by(Subject.id).all()
    return result