from database import Database
from config import DB_CONFIG

db = Database(**DB_CONFIG)

class Module:
  def __init__(self, moduleID, courseID, moduleTitle, moduleDescription):
    self.moduleID = moduleID
    self.courseID = courseID
    self.moduleTitle = moduleTitle
    self.moduleDescription = moduleDescription

  @staticmethod
  def returnModulesByCourseID(courseID):
    query = "SELECT * FROM Module WHERE courseID = ?"
    params = (courseID)
    result = db.execute_query(query, params)
    db.close()
    return result
  
  @staticmethod
  def updateModuleStatus(enrollmentID, moduleID):
    query = "UPDATE ModuleStatus SET moduleStatus = ? WHERE enrollmentID = ? AND moduleID = ?"
    params = ("Done", enrollmentID, moduleID)
    db.execute_query(query, params)

  @staticmethod
  def addModule(courseID):
    moduleTitle = input("Enter Module Title: ")
    moduleDescription = input("Enter Module Description: ")
    db.execute_query("INSERT INTO Module (courseID, moduleTitle, moduleDescription) VALUES (?,?,?)", (courseID, moduleTitle, moduleDescription))
    db.close()


