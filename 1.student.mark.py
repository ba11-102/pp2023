students = []
courses = []
marks = []

#data student
def input_info_student():
    print("------ENTER INFOR OF STUDENT------")
    id_student = input("Student ID : ")
    name_student = input("Student name : ")
    dob_student = input("Date of birth (a/b/c): ")
    return {
        'id_student': id_student,
        'name_student': name_student,
        'dob_student': dob_student,
        'marks': {}
    }
#input student
input_number_students = int(input("Enter the number of students: "))
for i in range(input_number_students):
    student = input_info_student()
    students.append(student)

#data course
def input_info_course():
    print("------ENTER INFOR OF COURSE------")
    id_course = input("Enter course ID: ")
    name_course = input("Enter course name: ")
    return {
        'id_course': id_course,
        'name_course': name_course
    }
#input course
input_number_courses = int(input("Enter the number of courses: "))
for i in range(input_number_courses):
    course = input_info_course()
    courses.append(course)


# input mark
def input_mark():
    list_courses()
    input_mark = input("ENTER MARK OF COURSE ID: ")
    for student in students:
        mark = int(input("Enter marks for  "+ student['name_student']))
        student['marks'][input_mark] = mark


# list of students
def list_students():
    for student in students:
        list_st = "ID:" + student['id_student'] + "       Name:" + student['name_student']
        print(list_st)


# list of course
def list_courses():
    for course in courses:
        list_course = "ID:" + course['id_course'] + "      Name:" + course['name_course']
        print(list_course)


def output_mark():
    list_courses()
    mark_of_student = input("SHOW MARK FOR COURSE ID: ")
    list_students()
    student_id = input("SHOW MARK FOR STUDENT ID: ")
    for student in students:
        if student['id_student'] == student_id:
            print(f"STUDENT: {student['name_student']}   MARK: {student['marks'][mark_of_student]}")


input_mark()

list_students()

list_courses()

output_mark()