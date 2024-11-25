from tabulate import tabulate
from database import Database
from config import DB_CONFIG

db = Database(**DB_CONFIG)

class Enrollment:
  enrollmentRecords = []

  def __init__(self, enrollmentID, studentID, courseID, enrollDate, status):
    self.enrollmentID = enrollmentID
    self.studentID = studentID
    self.courseID = courseID
    self.enrollDate = enrollDate
    self.status = status

  @staticmethod
  def getEnrollmentRecordByStudentID(studentID):
    query = "SELECT * FROM Enrollment WHERE studentID = ?"
    params = (studentID)
    result = db.execute_query(query, params)
    db.close()
    return result
  
  @classmethod
  def addToEnrollmentRecords(cls, records):
    for record in records:
      cls.enrollmentRecords.append(Enrollment(*record))

  @staticmethod
  def getCourseTitle(courseID):
    query = "SELECT * FROM Course WHERE courseID = ?"
    params = (courseID)
    result = db.execute_query(query, params, False)
    db.close()
    return result[1]
  
  @staticmethod
  def getCourseDescription(courseID):
    query = "SELECT * FROM Course WHERE courseID = ?"
    params = (courseID)
    result = db.execute_query(query, params, False)
    db.close()
    return result[2]

  @classmethod
  def displayStudentEnrolledRecords(cls, studentID):
    cls.enrollmentRecords = []
    records = Enrollment.getEnrollmentRecordByStudentID(studentID)
    Enrollment.addToEnrollmentRecords(records)
    headers = ["Number", "Title", "Description", "Status"]
    datas = []
    number = 1
    for enrollment in cls.enrollmentRecords:
      curData = []
      curData.append(number)
      number += 1
      curData.append(Enrollment.getCourseTitle(enrollment.courseID))
      curData.append(Enrollment.getCourseDescription(enrollment.courseID))
      curData.append(enrollment.status)
      datas.append(curData)
    print(tabulate(datas, headers=headers, tablefmt="rounded_grid"))

  #* MODULE TITLE | MODULE DESCRIPTION | STATUS 
  def displayModulesStatus(self):
    query = "SELECT Module.moduleTitle, Module.moduleDescription, ModuleStatus.moduleStatus FROM ModuleStatus JOIN Module ON ModuleStatus.moduleID = Module.moduleID WHERE enrollmentID = ?"
    params = (self.enrollmentID)
    results = db.execute_query(query,params)
    db.close()
    headers = ["Module Title", "Module Description", "Status"]
    datas = []
    for result in results:
      curData = []
      curData.append(result[0])
      curData.append(result[1])
      curData.append(result[2])
      datas.append(curData)
    print(tabulate(datas, headers=headers, tablefmt="rounded_grid"))


  

  

  