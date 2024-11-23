import copy
from tabulate import tabulate

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
  
  @staticmethod
  def displayStudentEnrolledRecords(studentID):
    headers = ["Number", "Course Title", "Progress", "Pending Assignments", "Status"] 
    records = Enrollment.getEnrollmentRecords(studentID)
    datas = []
    number = 1
    for record in records:
      curData = []
      curData.append(number)
      number += 1
      curData.append(record.enrolledCourse.courseTitle)
      curData.append(record.checkProgress())
      curData.append(len(record.assignments))
      curData.append("Completed" if record.completed == True else "Not Completed")
      datas.append(curData)
    print(tabulate(datas, headers=headers, tablefmt="rounded_grid"))
    # return datas

  