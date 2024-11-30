from quiz import Quiz

from tabulate import tabulate
from database import Database
from config import DB_CONFIG

from module import Module

db = Database(**DB_CONFIG)

class Course:
  allCourses = []
  instructorCourses = []

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
    

  @staticmethod
  def getAllCourses():
    query = "SELECT * FROM Course"
    result = db.execute_query(query)
    db.close()
    Course.addToAllCourses(result)
    Course.addCourseModules()

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
  
  #* INSTRUCTOR FUNCTIONS

  @classmethod
  def addInstructorCoursesModules(cls):
    for course in cls.instructorCourses:
      modules = Module.returnModulesByCourseID(course.courseID)
      for module in modules:
        course.courseModules.append(Module(*module))

  @classmethod
  def addToInstructorCourses(cls, records):
    for record in records:
      cls.instructorCourses.append(Course(*record))
    Course.addInstructorCoursesModules()
  
  @staticmethod
  def getCourseByInstructorID(instructorID):
      result = db.execute_query("SELECT * FROM Course WHERE instructorID = ?", (instructorID))
      db.close()
      return result

  @staticmethod
  def applyToCourse(courseID, instructorID):
    db.execute_query("UPDATE Course SET instructorID = ? WHERE courseID = ?", (instructorID, courseID))

  @classmethod
  def displayInstructingCourses(cls):
    header = ["Number", "Course Title", "Description", "Total Modules", "Total Students"]
    datas = []
    number = 1
    for course in cls.instructorCourses:
      curData = []
      curData.append(number)
      number += 1
      curData.append(course.courseTitle)
      curData.append(course.courseDescription)
      curData.append(course.displayModules())
      curData.append(course.totalStudents)
      datas.append(curData)
    print(tabulate(datas, header, tablefmt="rounded_grid"))

  @classmethod
  def displayAllModules(cls, courseIndex):
    course = cls.instructorCourses[courseIndex]
    header = ["Number", "Module Title", "Description", "Quiz"]
    datas = []
    for module in course.courseModules:
      curData = []
      curData.append(module.moduleID)
      curData.append(module.moduleTitle)
      curData.append(module.moduleDescription)
      curData.append("No Quiz" if Quiz.getQuizCount(module.moduleID) == 0 else "Quiz Created")
      datas.append(curData)
    print(tabulate(datas, header, tablefmt="rounded_grid"))






