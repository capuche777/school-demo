"""
Used to re-assign all the data, it must be executed every 24 hours
at 00:00:00 UTC
"""
from students.models import Student
from teachers.models import Teacher
from grades.models import Grade
from assignments.models import Assignment


def my_cron_job():
    """ List of tasks to execute """
    Student.objects.all().delete()
    Teacher.objects.all().delete()
    
    # Create Students
    Student.objects.create(
        id=1,
        name="Ashok",
        last_name="Kumar",
        gender="F",
        birthdate="1990-01-05"
    )

    
    Student.objects.create(
        id=2,
        name="Baby",
        last_name="Doe",
        gender="F",
        birthdate="1990-02-15"
    )

    Student.objects.create(
        id=3,
        name="Brett",
        last_name="Boe",
        gender="F",
        birthdate="1990-03-30"
    )

    Student.objects.create(
        id=4,
        name="Carla",
        last_name="Coe",
        gender="F",
        birthdate="1990-04-26"
    )

    Student.objects.create(
        id=5,
        name="Donna",
        last_name="Doe",
        gender="F",
        birthdate="1990-05-17"
    )

    Student.objects.create(
        id=6,
        name="Frank",
        last_name="Foe",
        gender="M",
        birthdate="1995-06-19"
    )

    Student.objects.create(
        id=7,
        name="Grace",
        last_name="Goe",
        gender="F",
        birthdate="1995-07-08"
    )

    Student.objects.create(
        id=8,
        name="Harry",
        last_name="Hoe",
        gender="M",
        birthdate="1995-08-05"
    )

    Student.objects.create(
        id=9,
        name="Jackie",
        last_name="Joe",
        gender="F",
        birthdate="1995-09-19"
    )

    Student.objects.create(
        id=10,
        name="Jane",
        last_name="Doe",
        gender="F",
        birthdate="1995-10-10"
    )

    Student.objects.create(
        id=11,
        name="Jane",
        last_name="Poe",
        gender="F",
        birthdate="1993-11-20"
    )

    Student.objects.create(
        id=12,
        name="Jane",
        last_name="Roe",
        gender="F",
        birthdate="1993-12-21"
    )

    Student.objects.create(
        id=13,
        name="Joe",
        last_name="Bloggs",
        gender="M",
        birthdate="1993-12-08"
    )

    Student.objects.create(
        id=14,
        name="Joe",
        last_name="Public",
        gender="M",
        birthdate="1993-11-25"
    )

    Student.objects.create(
        id=15,
        name="John",
        last_name="Doe",
        gender="M",
        birthdate="1996-10-20"
    )

    Student.objects.create(
        id=16,
        name="John",
        last_name="Noakes",
        gender="M",
        birthdate="1996-09-10"
    )

    Student.objects.create(
        id=17,
        name="John",
        last_name="Nokes",
        gender="M",
        birthdate="1996-08-30"
    )

    Student.objects.create(
        id=18,
        name="John",
        last_name="Q. Public",
        gender="M",
        birthdate="1996-07-30"
    )

    Student.objects.create(
        id=19,
        name="John",
        last_name="Smith",
        gender="M",
        birthdate="1996-06-22"
    )

    Student.objects.create(
        id=20,
        name="John",
        last_name="Stiles",
        gender="M",
        birthdate="1996-05-11"
    )

    # Create teachers
    Teacher.objects.create(id=1, name="John", last_name="A. Noakes", gender="M")
    Teacher.objects.create(id=2, name="John", last_name="A. Stiles", gender="M")
    Teacher.objects.create(id=3, name="Juan", last_name="Doe", gender="M")
    Teacher.objects.create(id=4, name="Karren", last_name="Koe", gender="F")
    Teacher.objects.create(id=5, name="Larry", last_name="Loe", gender="M")
    Teacher.objects.create(id=6, name="Mark", last_name="Moe", gender="M")
    Teacher.objects.create(id=7, name="Marta", last_name="Moe", gender="F")
    Teacher.objects.create(id=8, name="Mary", last_name="Major", gender="F")
    Teacher.objects.create(id=9, name="Norma", last_name="Noe", gender="F")
    Teacher.objects.create(id=10, name="Paula", last_name="Poe", gender="F")

    # Asign section and teacher to grade
    Grade.objects.create(id=1, name="First", teacher_id=1)
    Grade.objects.create(id=2, name="Second", teacher_id=2)
    Grade.objects.create(id=3, name="Third", teacher_id=3)
    Grade.objects.create(id=4, name="Fourth", teacher_id=4)
    Grade.objects.create(id=5, name="Fifth", teacher_id=5)

    # Assign students to grades
    Assignment.objects.create(id=1, section="A", student_id=1, grade_id=1)
    Assignment.objects.create(id=2, section="A", student_id=2, grade_id=1)
    Assignment.objects.create(id=3, section="A", student_id=3, grade_id=1)
    Assignment.objects.create(id=4, section="B", student_id=4, grade_id=1)
    Assignment.objects.create(id=5, section="B", student_id=5, grade_id=1)
    return True
