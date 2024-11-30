from tabulate import tabulate
from database import Database
from config import DB_CONFIG

from module import Module

db = Database(**DB_CONFIG)

class Course:
  allCourses = []

  def __init__(self, courseID,  courseTitle, courseDescription, instructorID, totalStudents):
    self.courseID = courseID
    self.courseTitle = courseTitle
    self.courseDescription = courseDescription
    self.instructorID = instructorID
    self.totalStudents = totalStudents

    self.courseModules = []
    self.certificate = "" # instance Certificate

  @classmethod
  def addCourseModules(cls):
    for course in cls.allCourses:
      modules = Module.returnModulesByCourseID(course.courseID)
      for module in modules:
        course.courseModules.append(Module(*module))

  @classmethod
  def addToAllCourses(cls, result):
    for row in result:
      cls.allCourses.append(Course(*row))
    Course.addCourseModules()

  @staticmethod
  def getAllCourses():
    query = "SELECT * FROM Course"
    result = db.execute_query(query)
    db.close()
    Course.addToAllCourses(result)

  def displayModules(self):
    string = ""
    for module in self.courseModules:
      string += f"{module.moduleTitle}\n"
    return string
  
  @staticmethod
  def getInstructorNameByID(instructorID):
    query = "SELECT * FROM Instructor WHERE instructorID = ?"
    params = (instructorID)
    result = db.execute_query(query, params, False)
    db.close()
    return result[3]

  def displayCourseDetails(self):
    headers = ["Title", "Description", "Instructor", "Modules", "Students"]
    datas = [[self.courseTitle, self.courseDescription, Course.getInstructorNameByID(self.instructorID), self.displayModules(), self.totalStudents]]
    print(tabulate(datas, headers=headers, tablefmt="rounded_grid"))

  @classmethod
  def displayCourses(cls):
    Course.allCourses = []
    Course.getAllCourses()
    headers = ["Number", "Course Title", "Description", "Intructor", "Total Modules", "Students Enrolled"]
    datas = []
    number = 1
    for course in cls.allCourses:
      currentData = []
      currentData.append(number)
      number += 1
      currentData.append(course.courseTitle)
      currentData.append(course.courseDescription)
      currentData.append(Course.getInstructorNameByID(course.instructorID))
      currentData.append(len(course.courseModules))
      currentData.append(course.totalStudents)
      datas.append(currentData)
    print(tabulate(datas, headers=headers, tablefmt="rounded_grid"))

  @staticmethod
  def getAllModules(courseID):
    query = "SELECT * FROM Module WHERE courseID = ?"
    params = (courseID)
    result = db.execute_query(query, params)
    db.close()
    return result





