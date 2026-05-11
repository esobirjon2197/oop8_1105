
# 8-m
class Student:
    def __init__(self, fullname, course):
        self.fullname = fullname
        self.course = course

    def study(self, subject):
        print(f"{self.fullname} {subject} fanini o‘qimoqda")


class Robot:
    def work(self):
        print("Robot ishlamoqda")


class University:
    def check_student(self, obj, subject):
        if hasattr(obj, "study"):
            obj.study(subject)
        else:
            print("study method topilmadi")


student = Student("Ali", 2)
robot = Robot()

uni = University()
uni.check_student(student, "Matematika")

uni.check_student(robot, "Matematika")
