from tabulate import tabulate

class Course:
  allCourses = []

  def __init__(self, courseTitle, courseDescription):
    self.courseTitle = courseTitle
    self.courseDescription = courseDescription
    self.courseInstructor = "None"
    self.courseModules = []
    self.certificate = "" # instance Certificate
    self.courseTotalStudents = 0

  @classmethod
  def getCourses(cls):
    headers = ["Number", "Course Title", "Description", "Intructor", "Total Modules", "Students Enrolled"]
    datas = []
    number = 1
    for course in cls.allCourses:
      currentData = []
      currentData.append(number)
      number += 1
      currentData.append(course.courseTitle)
      currentData.append(course.courseDescription)
      currentData.append(course.courseInstructor)
      currentData.append(len(course.courseModules))
      currentData.append(course.courseTotalStudents)
      datas.append(currentData)
    print(tabulate(datas, headers=headers, tablefmt="rounded_grid"))

  @classmethod
  def addToAllCourses(cls, course):
    cls.allCourses.append(course)

  def applyInstructor(self, instructor):
    self.courseInstructor = instructor

  def increaseTotalStudents(self):
    self.courseTotalStudents += 1

  def addCourseModules(self, module):
    self.courseModules.append(module)

  def displayModuleStatus(self):
    print(f"Course: {self.courseTitle}")
    for module in self.courseModules:
      print(f"Module: {module.moduleTitle} | Status: {module.moduleStatus}")

  def displayModules(self):
    string = ""
    for module in self.courseModules:
      string += f"{module.moduleTitle}\n"
    return string

  def checkModulesProgress(self):
    completed = 0
    for module in self.courseModules:
      if module.moduleStatus == "Done":
        completed += 1
    return completed
  
  def displayCourseDetails(self):
    headers = ["Title", "Description", "Instructor", "Modules", "Students"]
    datas = [[self.courseTitle, self.courseDescription, self.courseInstructor, self.displayModules(), self.courseTotalStudents]]
    print(tabulate(datas, headers=headers, tablefmt="rounded_grid"))
    

