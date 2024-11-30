from tabulate import tabulate
from database import Database
from config import DB_CONFIG
from course import Course

db = Database(**DB_CONFIG)

class Enrollment:
  enrollmentRecords = []

  def __init__(self, enrollmentID, studentID, courseID, enrollDate, status, assignmentID, assignmentStatus, grade):
    self.enrollmentID = enrollmentID
    self.studentID = studentID
    self.courseID = courseID
    self.enrollDate = enrollDate
    self.status = status
    self.assignmentID = assignmentID
    self.assignmentStatus = assignmentStatus
    self.grade = grade

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
    headers = ["Number", "Module Title", "Module Description", "Status"]
    datas = []
    number = 1
    for result in results:
      curData = []
      curData.append(number)
      number += 1
      curData.append(result[0])
      curData.append(result[1])
      curData.append(result[2])
      datas.append(curData)
    print(tabulate(datas, headers=headers, tablefmt="rounded_grid"))

  def getModules(self):
    # GET MODULES
    query = "SELECT Module.moduleID, ModuleStatus.moduleStatusID FROM ModuleStatus JOIN Module ON ModuleStatus.moduleID = Module.moduleID WHERE enrollmentID = ?"
    params = (self.enrollmentID)
    modulesID = db.execute_query(query, params)
    return modulesID
  
  @staticmethod
  def getModuleStatus(moduleStatusID):
    query = "SELECT * FROM ModuleStatus WHERE moduleStatusID = ?"
    params = (moduleStatusID)
    result = db.execute_query(query, params, False)
    db.close()
    return result
    
  @staticmethod
  def insertIntoModuleStatus(enrollmentID, courseID):
    print(enrollmentID, courseID)
    modules = Course.getAllModules(courseID)
    for module in modules:
      query = "INSERT INTO ModuleStatus (enrollmentID, moduleID, moduleStatus) VALUES (?,?,?)"
      params = (enrollmentID, module[0], "Not Done")
      db.execute_query(query, params)
      db.close() 
  
  @staticmethod
  def increaseStudentsEnrolled(courseID):
    query = "UPDATE Course SET totalStudents = totalStudents + 1 WHERE courseID = ?"
    params = (courseID)
    db.execute_query(query, params)
    # db.close()

  @staticmethod
  def getAssignmentIDByCourseID(courseID):
      query = "SELECT * FROM Assignment WHERE courseID = ?"
      params = (courseID)
      result = db.execute_query(query, params, False)
      db.close()
      return result[0]
  
  @staticmethod
  def enrollToCourse(studentID, courseID):
    assignmentID = Enrollment.getAssignmentIDByCourseID(courseID)
    query = "INSERT INTO Enrollment (studentID, courseID, enrollDate, status, assignmentID, assignmentStatus) OUTPUT INSERTED.enrollmentID, INSERTED.courseID VALUES (?,?,GETDATE(),?,?,?)"
    params = (studentID, courseID, "Not Complete", assignmentID, "Not Submitted")
    result = db.execute_query(query, params, False)
    print(result)
    Enrollment.increaseStudentsEnrolled(courseID)
    Enrollment.insertIntoModuleStatus(result[0], result[1])
    # Enrollment.insertIntoModuleStatus(18, )

  @staticmethod
  def updateEnrollmentStatus(enrollmentID):
    numberOfRecords = db.execute_query("SELECT COUNT(*) FROM ModuleStatus WHERE enrollmentID = ? AND moduleStatus = ?", (enrollmentID, "Not Done"), False)
    if numberOfRecords[0] == 0:
      db.execute_query("UPDATE Enrollment SET status = ? WHERE enrollmentID = ?", ("Complete", enrollmentID))
    db.close()




Enrollment.updateEnrollmentStatus(1)

    





  

  

  