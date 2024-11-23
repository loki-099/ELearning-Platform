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

global curUser
curUser = currentUser.current



def validateUser(username, password, userType):
  validatedUser = Person.validateUser(username, password, userType)
  currentUser.current = validatedUser
  if validatedUser == None:
    clear()
    print("NO USER FOUND")


#* STUDENT AND INSTRUCTOR PAGE #######################################################################################

def studentPage():
  print(f"Welcome, {curUser.fullName}")

def instructorPage():
  print(f"Welcome, {curUser.fullName}")

#* ###################################################################################################################


def main():
  choice = input("1 - Student LogIn\n2 - Instructor LogIn\n3 - Student Register\n4 - Instructor Register\n5 - Admin LogIn\n\nEnter choice: ")

  if choice == "1": #* STUDENT LOGIN
    username = input("Enter username: ")
    password = input("Enter password: ")
    validateUser(username, password, "Student")
    if curUser == None:
      main()
    elif curUser.userType == "Student":
      studentPage()
  elif choice == "2": #* INSTRUCTOR LOGIN
    username = input("Enter username: ")
    password = input("Enter password: ")
    validateUser(username, password, "Instructor")
    if curUser == None:
      main()
    elif curUser.userType == "Instructor":
      instructorPage()


# * SAMPLE DATA ####################################################################
student1 = Student("stud1", "stud1", "idol@email.com", "Luis Tolentino", "2004-06-13", "Davao Del Sur", "Male")
student2 = Student("stud2", "stud2", "idol@email.com", "Jhon Tolentino", "2004-06-13", "Davao Del Sur", "Male")
instructor = Instructor("inst1", "inst1", "inst@email.com", "Lloyd Tolentino", "2004-06-12", "Purok 5", "Male")

Person.addToListOfUsers(student1)
Person.addToListOfUsers(student2)
Person.addToListOfUsers(instructor)

main()
