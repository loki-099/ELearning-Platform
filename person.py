from abc import ABC, abstractmethod
from database import Database
from config import DB_CONFIG

db = Database(**DB_CONFIG)

class Person(ABC):

  def __init__(self, id, username, password, fullName, email, gender, birthDate, address):
    self.id = id
    self.username = username
    self.password = password
    self.email = email
    self.fullName = fullName
    self.birthDate = birthDate
    self.address = address
    self.gender = gender

  @abstractmethod
  def getDetails(self):
    pass

  @staticmethod
  def validateEmail(email):
    return True if "@" in email else False
  
  def getAge(self):
    pass


class Student(Person):
  userType = "Student"
  def __init__(self, id, username, password, fullName, email, gender, birthDate, address):
    super().__init__(id, username, password, fullName, email, gender, birthDate, address)
    self.enrolledCourses = []
    self.earnedCertificates = []
    self.assignments = []

  @classmethod
  def getUserType(cls):
    return cls.userType
  
  @staticmethod
  def registerToDB(username, password, fullName, email, gender, birthDate, address):
    query = "INSERT INTO Student (username, password, fullName, email, gender, birthDate, address) VALUES (?,?,?,?,?,?,?)"
    params = (username, password, fullName, email, gender, birthDate, address)
    db.execute_query(query, params)
    db.close()
  
  @staticmethod
  def validateStudent(username, password):
    query = f"SELECT * FROM Student WHERE username = ? AND password = ?"
    params = (username, password)
    result = db.execute_query(query, params, False)
    db.close()
    return result

  def getDetails(self):
    pass

  def gainCertificate(self):
    pass


class Instructor(Person):
  userType = "Instructor"

  def __init__(self, id, username, password, fullName, email, gender, birthDate, address):
    super().__init__(id, username, password, fullName, email, gender, birthDate, address)
    self.offeredCourses = []
    self.credentials = []

  @classmethod
  def getUserType(cls):
    return cls.userType
  
  def getDetails(self):
    pass

