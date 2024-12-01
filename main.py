from person import Person, Student, Instructor
from course import Course
from module import Module
from enrollment import Enrollment
from quiz import Quiz
from assignment import Assignment
from schedule import Schedule
from grade import Grade
from platformadmin import PlatformAdmin
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
        clear()
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
  print("ASSIGNMENTS")
  Assignment.displayAssignments(currentUser.current.id)
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
    
#* #####################################################################################################################

#* INSTRUCTOR PAGE

def viewCoursesInstructor(): #* VIEW COURSES PAGE
  print("COURSES AVAILABLE")
  Course.displayCourses()
  choice = input("1 - View Course Details\n0 - Back\n\nEnter choice: ")

  if choice == "1": #* VIEW COURSE DETAILS
    courseIndex = int(input("Enter Course Number: ")) - 1
    clear()
    print("COURSE DETAILS")
    course = Course.allCourses[courseIndex]
    course.displayCourseDetails()
    choice = input("1 - Apply as Instructor\n0 - Back\n\nEnter choice: ")

    if choice == "1": #* APPLY AS INTRUCTOR
      if any(record.courseID == course.courseID for record in Course.instructorCourses):
        clear()
        print("Already applied as Instructor")
        viewCoursesInstructor()
      else:
        Course.applyToCourse(course.courseID, currentUser.current.id)
        clear()
        print("APPLIED TO COURSE")
        instructorPage()

    elif choice == "0":
      clear()
      viewCoursesInstructor()

  elif choice == "0": #* BACK TO INSTRUCTOR PAGE
    clear()
    instructorPage()

def viewModules(courseIndex): #* VIEW MODULES PAGE
  Course.displayAllModules(courseIndex)
  choice = input("1 - Add Module\n2 - Create Quiz\n0 - Back\n\nEnter your choice: ")
  courseID = Course.instructorCourses[courseIndex].courseID

  if choice == "1": #* ADD MODULE
    Module.addModule(courseID)
    clear()
    print("MODULE ADDED")
    instructorPage()

  if choice == "2": #* ADD QUIZ
    moduleID = int(input("Enter Module Number: "))
    Quiz.createQuiz(moduleID)
    # clear()
    print("QUIZ CREATED")
    instructorPage()

  elif choice == "0": #* BACK TO INSTRUCTING COURSES
    clear()
    viewInstructingCourses()

def viewAssignmentsInstructor(courseIndex):
  courseID = Course.instructorCourses[courseIndex].courseID
  Assignment.displayAssignmentStatus(courseID)
  choice = input("0 - Back\n\nEnter your choice: ")

  if choice == "1":
    pass

  elif choice == "0":
    clear()
    viewInstructingCourses()


def viewSchedules(courseIndex):
  courseID = Course.instructorCourses[courseIndex].courseID
  Schedule.displayInstructedCourseSchedules(courseID)
  choice = input("1 - Add Schedule\n0 - Back\n\nEnter choice: ")

  if choice == "1": 
    Schedule.addSchedule(courseID)
    clear()
    print("SCHEDULE ADDED")
    viewInstructingCourses()

  elif choice == "0":
    clear()
    viewInstructingCourses()


def viewStudents(courseIndex):
  courseID = Course.instructorCourses[courseIndex].courseID
  Enrollment.displayStudents(courseID)
  choice = input("1 - Give Grade\n0 - Back\n\nEnter choice: ")

  if choice == "1":
    studentID = int(input("Enter Student ID: "))
    Grade.giveGrade(courseID, studentID)
    clear()
    print("GRADE GIVEN")
    viewInstructingCourses()

  elif choice == "0":
    clear()
    viewInstructingCourses()


def viewInstructingCourses(): #* VIEW INSTRUCTING COURSES PAGE  
  print("INSTRUCTING COURSES")
  Course.displayInstructingCourses()
  choice = input("1 - View Modules\n2 - View Assignments\n3 - View Schedules\n4 - View Students\n0 - Back\n\nEnter choice: ")

  if choice == "1": #* VIEW MODULES PAGE
    courseIndex = int(input("Enter Course Number: ")) - 1
    clear()
    viewModules(courseIndex)

  elif choice == "2": #* VIEW ASSIGNMENTS PAGE
    courseIndex = int(input("Enter Course Number: ")) - 1
    clear()
    viewAssignmentsInstructor(courseIndex)

  elif choice == "3": #* VIEW SCHEDULES PAGE
    courseIndex = int(input("Enter Course Number: ")) - 1
    clear()
    viewSchedules(courseIndex)

  elif choice == "4": #* VIEW STUDENTS PAGE
    courseIndex = int(input("Enter Course Number: ")) - 1
    clear()
    viewStudents(courseIndex)

  elif choice == "0": #* BACK TO INSTRUCTOR PAGE
    clear()
    instructorPage()




def instructorPage():
  Course.instructorCourses = []
  Course.addToInstructorCourses(Course.getCourseByInstructorID(currentUser.current.id))
  print(f"Welcome, {currentUser.current.fullName}")
  choice = input("1 - View Courses\n2 - View Courses Instructing\n0 - LogOut\n\nEnter choice: ")

  if choice == "1": #* VIEW COURSES
    clear()
    viewCoursesInstructor()

  elif choice == "2": #* VIEW INSTRUCTING COURSES
    clear()
    viewInstructingCourses()

  elif choice == "0": #* BACK TO MAIN
    clear()
    main()

#* ###################################################################################################################

#* ADMIN PAGE

def viewCoursesAdmin(): #* ADMIN VIEW COURSES PAGE
  admin = currentUser.current
  admin.displayAllCourses()
  choice = input("1 - Add Course\n2 - Remove Course\n0 - Back\n\nEnter choice: ")

  if choice == "1":
    admin.addCourse()
    clear()
    print("COURSE ADDED")
    viewCoursesAdmin()

  elif choice == "2":
    courseID = int(input("Enter Course ID: "))
    confirmation = input("All Records will be Deleted, are you sure?(y/n): ")
    if confirmation.lower() == "y":
      admin.removeCourse(courseID)
      clear()
      print("ALL RECORDS ARE DELETED")
      viewCoursesAdmin()
    else:
      clear()
      print("CANCELLED")
      viewCoursesAdmin()

  elif choice == "0":
    clear()
    adminPage()

def viewUsers():
  admin = currentUser.current
  choice = input("1 - View Students\n2 - View Instructors\n0 - Back\n\nEnter choice: ")

  if choice == "1": #* VIEW STUDENTS
    clear()
    admin.displayAllUsers(choice)
    choice = input("1 - Remove Student\n0 - Back\n\nEnter choice: ")
    
    if choice == "1":
      studentID = int(input("Enter Student ID: "))
      admin.removeStudent(studentID)
      clear()
      print("STUDENT REMOVED")
      viewUsers()

    elif choice == "0":
      clear()
      viewUsers()

  elif choice == "2": #* VIEW INSTRUCTORS
    clear()
    admin.displayAllUsers(choice)
    choice = input("1 - Remove Instructor\n0 - Back\n\nEnter choice: ")
    
    if choice == "1":
      instructorID = int(input("Enter Instructor ID: "))
      admin.removeInstructor(instructorID)
      clear()
      print("INSTRUCTOR REMOVED")
      viewUsers()

    elif choice == "0":
      clear()
      viewUsers()
    

  elif choice == "0":
    clear()
    adminPage()



def adminPage(): #* ADMIN PAGE
  print("WELCOME, ADMIN")
  choice = input("1 - View Courses\n2 - View Users\n0 - LogOut\n\nEnter choice: ")

  if choice == "1": #* ADMIN VIEW COURSES
    clear()
    viewCoursesAdmin()

  elif choice == "2":
    clear()
    viewUsers()

  elif choice == "0":
    clear()
    main()
  



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
    result = Instructor.validateInstructor(username, password)
    if not result:
      clear()
      print("NO USER FOUND")
      main()
    elif result:
      currentUser.current = Instructor(*result)
      clear()
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

  elif choice == "4": #* INSTRUCTOR REGISTER
    print("INSTRUCTOR REGISTER")
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
    Instructor.registerToDB(username, password, fullName, email, gender, birthDate, address)
    main()

  elif choice == "5": #* ADMIN LOGIN
    print("ADMIN LOGIN")
    username = input("Enter username: ")
    password = input("Enter password: ")
    result = PlatformAdmin.validateAdmin(username, password)
    if not result:
      clear()
      print("INVALID CREDENTIALS")
      main()
    elif result:
      currentUser.current = PlatformAdmin(*result)
      clear()
      adminPage()

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
