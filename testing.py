from person import Person, Student, Instructor
from course import Course
from module import Module
from enrollment import Enrollment

student1 = Student("stud1", "stud1", "idol@email.com", "Luis Tolentino", "2004-06-13", "Davao Del Sur", "Male")
student2 = Student("stud2", "stud2", "idol@email.com", "Jhon Tolentino", "2004-06-13", "Davao Del Sur", "Male")
instructor = Instructor("inst1", "inst1", "inst@email.com", "Lloyd Tolentino", "2004-06-12", "Purok 5", "Male")

course1 = Course("How To Become AI Coder", "AI Coder ampota")
course2 = Course("Howt To Die Peacefully", "yawa nga case study")

Course.addToAllCourses(course1)
Course.addToAllCourses(course2)

module1 = Module("Module 1", "Yawa oy", "Not Done")
course1.addCourseModules(module1)
module2 = Module("Module 2", "Di na ko", "Done")
course1.addCourseModules(module2)

# print(Course.getCourses())
# Course.getCourses()
# course1.displayModules()

enrollment1 = Enrollment(student1, course1)
Enrollment.addToEnrollmentRecords(enrollment1)
enrollment2 = Enrollment(student1, course2)
Enrollment.addToEnrollmentRecords(enrollment2)
# print(enrollment1.checkProgress())
# enrollment1.enrolledCourse.courseInstructor = "Lloyd"
# print(enrollment1.enrolledCourse.courseInstructor)
# print(course1.courseInstructor)
studentRecord = Enrollment.getEnrollmentRecords(student1.studentID)
for record in studentRecord:
  print(f"Course: {record.enrolledCourse.courseTitle} | {record.checkProgress()}")


