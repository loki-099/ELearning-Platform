from person import Person, Student, Instructor
from course import Course
from module import Module
from enrollment import Enrollment
from quiz import Quiz
from assignment import Assignment
from schedule import Schedule
from grade import Grade
from tabulate import tabulate
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

def takeQuiz(moduleToQuiz, enrollmentRecordID): #* TAKE QUIZ PAGE
  moduleID = moduleToQuiz
  isPass = Quiz.doQuiz(moduleID)
  if isPass:
    Module.updateModuleStatus(enrollmentRecordID, moduleID)
    Enrollment.updateEnrollmentStatus(enrollmentRecordID)
    print("You passed the Quiz! Congrats lods!")
    input("Enter any key to back: ") 
    clear()
    viewEnrolledCourses()
  else:
    print("Pass the Quiz to Complete this Module!")
    input("Enter any key to back: ")  
    clear()
    viewEnrolledCourses()
  
  

def viewCourses(): #* VIEWCOURSES PAGE
  print("COURSES AVAILABLE")
  Course.displayCourses()
  choice = input("1 - View Course Details\n0 - Back\n\nEnter choice: ")

  if choice == "1": #* VIEW COURSE DETAILS
    courseIndex = int(input("Enter Course Number: ")) - 1
    clear()
    print("COURSE DETAILS")
    course = Course.allCourses[courseIndex]
    course.displayCourseDetails()
    choice = input("1 - Enroll to Course\n0 - Back\n\nEnter choice: ")

    if choice == "1": #* ENROLL TO COURSE
      Enrollment.addToEnrollmentRecords(Enrollment.getEnrollmentRecordByStudentID(currentUser.current.id))
      if any(record.courseID == course.courseID for record in Enrollment.enrollmentRecords):
        clear()
        print("Already Enrolled")
        viewCourses()
      else:
        Enrollment.enrollToCourse(currentUser.current.id, course.courseID)
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
  Enrollment.displayStudentEnrolledRecords(currentUser.current.id)
  choice = input("1 - View Modules\n0 - Back\n\nEnter choice: ")

  if choice == "1": #* VIEW MODULES
    index = int(input("Enter Course Number: ")) - 1
    clear()
    print("COURSE MODULES")
    enrollmentRecordID = Enrollment.enrollmentRecords[index].enrollmentID
    Enrollment.enrollmentRecords[index].displayModulesStatus()
    choice = input("1 - Take Quiz\n0 - Back\n\nEnter choice: ")

    if choice == "1": #* TAKE QUIZ
      modules = Enrollment.enrollmentRecords[index].getModules()
      index = int(input("Enter Module Number: ")) - 1
      moduleStatus = Enrollment.getModuleStatus(modules[index][1])
      if not moduleStatus[3] == "Done":
        clear()
        takeQuiz(modules[index][0], enrollmentRecordID)
      else:
        clear()
        print("Already took a quiz!")
        viewEnrolledCourses()
    elif choice == "0":
      clear()
      viewEnrolledCourses()


  elif choice == "0": #* BACK TO STUDENT PAGE
    clear()
    studentPage()


def viewAssignments(): #* VIEW ASSIGNMENTS PAGE
  Assignment.displayAssignments(currentUser.current.id)
  print("ASSIGNMENTS")
  choice = input("1 - Submit Assignment\n0 - Back\n\nEnter choice: ")

  if choice == "1":
    enrollmentID = int(input("Enter Assignment Number: "))
    Assignment.submitAssignment(enrollmentID)
    clear()
    print("Assignment Submitted")
    viewAssignments()
  elif choice == "0":
    clear()
    studentPage()




def studentPage(): 
  Enrollment.enrollmentRecords = []
  Enrollment.addToEnrollmentRecords(Enrollment.getEnrollmentRecordByStudentID(currentUser.current.id))
  currentStudent = currentUser.current
  print(f"Welcome, {currentStudent.fullName}")
  choice = input("1 - View Courses\n2 - View Enrolled Courses\n3 - View Assignments\n4 - View Schedules\n5 - View Grades\n0 - LogOut\n\nEnter choice: ")

  if choice == "1": #* VIEW COURSES
    clear()
    viewCourses()

  elif choice == "2": #* VIEW ENROLLED COURSES
    clear()
    viewEnrolledCourses()

  elif choice == "3": #* VIEW ASSIGNMENTS
    clear()
    viewAssignments()

  elif choice == "4": #* VIEW SCHEDULES
    clear()
    print("SCHEDULES")
    Schedule.displaySchedules()
    input("Enter any key to back: ")
    clear()
    studentPage()

  elif choice == "5": #* VIEW GRADES
    clear()
    print("GRADES")
    Grade.displayGrades()
    input("Enter any key to back: ")
    clear()
    studentPage()

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
    result = Student.validateStudent(username, password)
    if not result:
      clear()
      print("NO USER FOUND")
      main()
    elif result:
      currentUser.current = Student(*result)
      clear()
      studentPage()

  elif choice == "2": #* INSTRUCTOR LOGIN
    username = input("Enter username: ")
    password = input("Enter password: ")
    validateUser(username, password, "Instructor")
    if currentUser.current == None:
      main()
    elif currentUser.current.userType == "Instructor":
      instructorPage()

  elif choice == "3": #* STUDENT REGISTER
    print("STUDENT REGISTER")
    username = input("Enter username: ")
    password = input("Enter password: ")
    fullName = input("Enter Full Name: ")
    while True:
      email = input("Enter email: ")
      if Person.validateEmail(email):
        break
      print("Invalid Email Format. Try again!")
    gender = input("Enter gender: ")
    birthDate = input("Enter birthdate('yyyy-mm-dd'): ")
    address = input("Enter address: ")
    Student.registerToDB(username, password, fullName, email, gender, birthDate, address)
    main()



  else:
    clear()
    main()


# * SAMPLE DATA ####################################################################
# student1 = Student("stud1", "stud1", "idol@email.com", "Luis Tolentino", "2004-06-13", "Davao Del Sur", "Male")
# student2 = Student("stud2", "stud2", "idol@email.com", "Jhon Tolentino", "2004-06-13", "Davao Del Sur", "Male")
# instructor = Instructor("inst1", "inst1", "inst@email.com", "Lloyd Tolentino", "2004-06-12", "Purok 5", "Male")

# Person.addToListOfUsers(student1)
# Person.addToListOfUsers(student2)
# Person.addToListOfUsers(instructor)

# course1 = Course("How To Become AI Coder", "AI Coder ampota")
# course2 = Course("Howt To Die Peacefully", "yawa nga case study")

# Course.addToAllCourses(course1)
# Course.addToAllCourses(course2)

# module1 = Module("Module 1", "Yawa oy", "Not Done")
# course1.addCourseModules(module1)
# module2 = Module("Module 2", "Di na ko", "Not Done")
# course1.addCourseModules(module2)

main()
