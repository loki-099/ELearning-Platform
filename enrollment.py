import copy

class Enrollment:
  enrollmentRecords = []

  def __init__(self, enrolledStudent, enrolledCourse):
    self.enrolledStudent = enrolledStudent
    self.enrolledCourse = copy.deepcopy(enrolledCourse)
    self.progress = ""
    self.completed = False
    self.assignments = []
    self.quizzes = []

  def checkProgress(self):
    self.enrolledCourse.checkModulesProgress()
    return f"Completed: {self.enrolledCourse.checkModulesProgress()}/{len(self.enrolledCourse.courseModules)}"
  
  @classmethod
  def addToEnrollmentRecords(cls, record):
    cls.enrollmentRecords.append(record)

  @classmethod
  def getEnrollmentRecords(cls, studentID):
    records = []
    for enrollmentRecord in cls.enrollmentRecords:
      if studentID == enrollmentRecord.enrolledStudent.studentID:
        records.append(enrollmentRecord)
    return records

