from abc import ABC, abstractmethod
import random
import string
import json

def loadData(filePath):
    try:
        with open(filePath, 'r') as file:
            data = json.load(file)

            # Convert to appropriate instances based on userType
            # instances = []
            for entry in data:
                if entry["userType"] == "Student":
                    # instances.append(Student.from_dict(entry))
                    Person.addToListOfUsers(Student.from_dict(entry))
                elif entry["userType"] == "Instructor":
                    # instances.append(Instructor.from_dict(entry))
                    Person.addToListOfUsers(Instructor.from_dict(entry))
                else:
                    print(f"Warning: Unknown userType '{entry['userType']}' for username '{entry['username']}'")
            # return instances

    except FileNotFoundError:
        print("Error: File not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return []
    
def addPersonToData(instance):
  pass


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
  
  @staticmethod
  def from_dict(data):
    return Person(
      data["username"],
      data["password"],
      data["email"],
      data["fullName"],
      data["birthdate"],
      data["address"],
      data["gender"],
      data["userType"]
    )
  
  @classmethod
  def updateData(cls):
    loadData('./database/person.json')
    
  
  
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
  
  @staticmethod
  def from_dict(data):
    return Student(
      data["username"],
      data["password"],
      data["email"],
      data["fullName"],
      data["birthdate"],
      data["address"],
      data["gender"]
    )
  
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
  
  @staticmethod
  def from_dict(data):
      return Instructor(
          data["username"],
          data["password"],
          data["email"],
          data["fullName"],
          data["birthdate"],
          data["address"],
          data["gender"]
      )

  
  def getDetails(self):
    pass

