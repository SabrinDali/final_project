import uuid

"""ITF 07 Final Project Attendance System
# TODO 1 Enter your name and submission date
Name : Sabrin Ahmed Al Dali
Delivery Date : 25.06.2023
"""


# TODO 2 Define Course Class and define constructor with
# course_id (generated using uuid4) ,
# course name (user_input) and
# course mark (user_input)

class Course:

    def __init__(self, course_name, course_mark):
        self.course_id = str(uuid.uuid4())
        self.course_name = course_name
        self.course_mark = course_mark


# TODO 3 define static variable indicates total student count

# TODO 4 define a constructor which includes
# student_id (unique using uuid module)
# student_name (user input)
# student_age (user input)
# student_number (user_input)
# courses_list (List of Course Objects)
class Student:
    total_student = 0

    def __init__(self, student_name, student_age, student_number):
        self.student_id = str(uuid.uuid4())
        self.name = input(student_name)
        self.age = int(input(student_age))
        self.number = int(input(student_number))
        self.courses_list = []
        Student.total_student += 1

    def enroll_course(self, course_name, course_mark):
        course = Course(course_name, course_mark)
        self.courses_list.append(course)

    # TODO 5 define a method to enroll new course to student courses list

    # method to get_student_details as dict
    def get_student_details(self):
        return {
            "student_id": self.student_id,
            "student_name": self.name,
            "student_age": self.age,
            "student_number": self.number,
            "courses_list": [course.__dict__ for course in self.courses_list]
        }

    # method to get_student_courses
    def get_student_courses(self):
        for course in self.courses_list:
            print(f"Course Name: {course.course_name}, Course Mark: {course.course_mark}")

        # TODO 6 print student courses with their marks

    # method to get student_average as a value
    def get_student_average(self):
        total_marks = 0
        for course in self.courses_list:
            total_marks += course.course_mark
        return total_marks / len(self.courses_list) if len(self.courses_list) > 0 else 0

        # TODO 7 return the student average


# in Global Scope
# TODO 8 declare empty students list

students_list = []

while True:

    # TODO 9 handle Exception for selection input
    selection = int(input("1.Add New Student\n"
                          "2.Delete Student\n"
                          "3.Display Student\n"
                          "4.Get Student Average\n"
                          "5.Add Course to student with mark.\n"
                          "6.Exit"))

    if selection == 1:
        student_number = input("Enter Student Number")

        if any(student.student_number == student_number for student in students_list):
            print("Student number already exists.")
            continue

        # TODO 10 make sure that Student number is not exists before

        student_name = input("Enter Student Name")
        while True:
            try:
                student_age = int(input("Enter Student Age"))
                break
            except:
                print("Invalid Value")
        student = Student(student_name, student_age, student_number)
        students_list.append(student)
        print("Student Added Successfully")

        # TODO 11 create student object and append it to students list


    elif selection == 2:
        student_number = input("Enter Student Number")
        for student in students_list:
                if student.student_number == student_number:
                    students_list.remove(student)
                    print("Student Deleted Successfully")
                    break
        else:
            print("Student Not Exist")

        # TODO 12 find the target student using loops and delete it if exist , if not print ("Student Not Exist")

    elif selection == 3:
        student_number = input("Enter Student Number")
        for student in students_list:
            if student.student_number == student_number:
                print(student.get_student_details())
                break
        else:
            print("Student Not Exist")

        # TODO 13 find the target student using loops and print student detials  if exist , if not print ("Student Not Exist")

    elif selection == 4:
        student_number = input("Enter Student Number")
        for student in students_list:
            if student.student_number == student_number:
                print(f"Student Average: {student.get_student_average()}")
                break
        else:
            print("Student Not Exist")

        # TODO 14 find the target student using loops and get student average  if exist , if not print ("Student Not Exist")

    elif selection == 5:
        student_number = input("Enter Student Number")
        for student in students_list:
            if student.student_number == student_number:
                course_name = input("Enter Course Name")
                while True:
                    try:
                        course_mark = int(input("Enter Course Mark"))
                        break
                    except:
                        print("Invalid Value")
                student.enroll_course(course_name, course_mark)
                print("Course Added Successfully")
                break
        else:
            print("Student Not Exist")

    elif selection == 6:
        break

        else:
        print("Invalid Selection")

    except ValueError:
    print("Invalid Selection")


        # TODO 15 ask user to enter course name and course mark then create coures object then append it to target student courses



# TODO 16 call a function to exit the program

