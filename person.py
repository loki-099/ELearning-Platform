from abc import ABC, abstractmethod
import random
import string

class Person(ABC):
  listOfUsers = []

  def __init__(self, username, password, email, fullName, birthdate, address, gender, userType):
    self.username = username
    self.password = password
    self.email = email
    self.fullName = fullName
    self.birthdate = birthdate
    self.address = address
    self.gender = gender
    self.userType = userType

  @classmethod
  def addToListOfUsers(cls, user):
    cls.listOfUsers.append(user)

  @classmethod
  def validateUser(cls, username, password, userType):
    for user in cls.listOfUsers:
      if username == user.username and password == user.password and userType == user.userType:
        return user
    return None

  @abstractmethod
  def getDetails(self):
    pass

  @staticmethod
  def validateEmail(email):
    return True if "@" in email else False
  
  @staticmethod
  def generateID():
    characters = string.ascii_letters + string.digits
    random_id = ''.join(random.choices(characters, k=5))
    return random_id
  
  def getAge(self):
    pass


class Student(Person):
  userType = "Student"

  def __init__(self, username, password, email, fullName, birthdate, address, gender):
    super().__init__(username, password, email, fullName, birthdate, address, gender, Student.getUserType())
    self.studentID = Person.generateID()
    self.enrolledCourses = []
    self.earnedCertificates = []
    self.assignments = []

  @classmethod
  def getUserType(cls):
    return cls.userType
  
  def getDetails(self):
    pass

  def gainCertificate(self):
    pass


class Instructor(Person):
  userType = "Instructor"

  def __init__(self, username, password, email, fullName, birthdate, address, gender):
    super().__init__(username, password, email, fullName, birthdate, address, gender, Instructor.getUserType())
    self.instructorID = Person.generateID()
    self.offeredCourses = []
    self.credentials = []

  @classmethod
  def getUserType(cls):
    return cls.userType
  
  def getDetails(self):
    pass

