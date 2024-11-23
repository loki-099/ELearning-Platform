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
    for course in cls.allCourses:
      print(f"Course Title: {course.courseTitle}")

  @classmethod
  def addToAllCourses(cls, course):
    cls.allCourses.append(course)

  def applyInstructor(self, instructor):
    self.courseInstructor = instructor

  def increaseTotalStudents(self):
    self.courseTotalStudents += 1

  def addCourseModules(self, module):
    self.courseModules.append(module)

  def displayModules(self):
    print(f"Course: {self.courseTitle}")
    for module in self.courseModules:
      print(f"Module: {module.moduleTitle} | Status: {module.moduleStatus}")

  def checkModulesProgress(self):
    completed = 0
    for module in self.courseModules:
      if module.moduleStatus == "Done":
        completed += 1
    return completed

