from person import Person, Student, Instructor
from course import Course
from module import Module
from enrollment import Enrollment
from os import system, name

def clear(): #* clearing terminals

  if name == 'nt': #* for windows
    _ = system('cls')
  else: # for mac and linux
    _ = system('clear')

class currentUser:
  current = None

global currentStudent
currentStudent = None  

def validateUser(username, password, userType):
  currentUser.current = Person.validateUser(username, password, userType)
  if currentUser.current == None:
    clear()
    print("NO USER FOUND")


#* STUDENT AND INSTRUCTOR PAGE #######################################################################################

#* STUDENT PAGES: 

def viewCourses(): #* VIEWCOURSES PAGE
  print("COURSES AVAILABLE")
  Course.getCourses()
  choice = input("1 - View Course Details\n0 - Back\n\nEnter choice: ")

  if choice == "1": #* VIEW COURSE DETAILS
    courseIndex = int(input("Enter Course Number: ")) - 1
    clear()
    print("COURSE DETAILS")
    course = Course.allCourses[courseIndex]
    course.displayCourseDetails()
    choice = input("1 - Enroll to Course\n0 - Back\n\nEnter choice: ")

    if choice == "1": #* ENROLL TO COURSE
      newEnrollmentRecord = Enrollment(currentUser.current, course)
      Enrollment.addToEnrollmentRecords(newEnrollmentRecord)
      print("ENROLLED TO COURSE")
      studentPage()
    elif choice == "0": #* BACK TO VIEWCOURSES PAGE
      clear()
      viewCourses()
    
  elif choice == "0": #* BACK TO STUDENTPAGE
    clear()
    studentPage()

def viewEnrolledCourses(): #* VIEW ENROLLEDCOURSES PAGE
  print("ENROLLED COURSES")
  Enrollment.displayStudentEnrolledRecords(currentUser.current.studentID)
  choice = input("1 - View Modules\n0 - Back\n\nEnter choice: ")

  if choice == "1": #* VIEW MODULES
    pass

  elif choice == "0": #* BACK TO STUDENT PAGE
    clear()
    studentPage()









def studentPage(): 
  currentStudent = currentUser.current
  clear()
  print(f"Welcome, {currentStudent.fullName}")
  choice = input("1 - View Courses\n2 - View Enrolled Courses\n3 - View Assignments\n4 - View Schedules\n0 - LogOut\n\nEnter choice: ")

  if choice == "1": #* VIEW COURSES
    clear()
    viewCourses()

  elif choice == "2": #* VIEW ENROLLED COURSES
    clear()
    viewEnrolledCourses()

  elif choice == "0": #* BACK TO MAIN
    clear()
    main()
    


def instructorPage():
  print(f"Welcome, {currentUser.current.fullName}")

#* ###################################################################################################################


def main():
  choice = input("1 - Student LogIn\n2 - Instructor LogIn\n3 - Student Register\n4 - Instructor Register\n5 - Admin LogIn\n\nEnter choice: ")

  if choice == "1": #* STUDENT LOGIN
    username = input("Enter username: ")
    password = input("Enter password: ")
    validateUser(username, password, "Student")
    if currentUser.current == None:
      main()
    elif currentUser.current.userType == "Student":
      studentPage()

  elif choice == "2": #* INSTRUCTOR LOGIN
    username = input("Enter username: ")
    password = input("Enter password: ")
    validateUser(username, password, "Instructor")
    if currentUser.current == None:
      main()
    elif currentUser.current.userType == "Instructor":
      instructorPage()

  else:
    clear()
    main()


# * SAMPLE DATA ####################################################################
student1 = Student("stud1", "stud1", "idol@email.com", "Luis Tolentino", "2004-06-13", "Davao Del Sur", "Male")
student2 = Student("stud2", "stud2", "idol@email.com", "Jhon Tolentino", "2004-06-13", "Davao Del Sur", "Male")
instructor = Instructor("inst1", "inst1", "inst@email.com", "Lloyd Tolentino", "2004-06-12", "Purok 5", "Male")

Person.addToListOfUsers(student1)
Person.addToListOfUsers(student2)
Person.addToListOfUsers(instructor)

course1 = Course("How To Become AI Coder", "AI Coder ampota")
course2 = Course("Howt To Die Peacefully", "yawa nga case study")

Course.addToAllCourses(course1)
Course.addToAllCourses(course2)

module1 = Module("Module 1", "Yawa oy", "Not Done")
course1.addCourseModules(module1)
module2 = Module("Module 2", "Di na ko", "Done")
course1.addCourseModules(module2)

main()
