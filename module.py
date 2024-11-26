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


