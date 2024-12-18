from tabulate import tabulate
from database import Database
from config import DB_CONFIG

db = Database(**DB_CONFIG)

class PlatformAdmin:

    def __init__(self, adminID, username, password, fullName, email):
        self.adminID = adminID
        self.username = username
        self.password = password
        self.fullName = fullName
        self.email = email

    @staticmethod
    def validateAdmin(username, password):
        query = f"SELECT * FROM PlatformAdmin WHERE username = ? AND password = ?"
        params = (username, password)
        result = db.execute_query(query, params, False)
        db.close()
        return result
    
    def displayAllCourses(self):   
        results = db.execute_query("SELECT Course.courseID, Course.courseTitle, Course.courseDescription, Instructor.fullName, Course.totalStudents FROM Course LEFT JOIN Instructor ON Instructor.instructorID = Course.instructorID")
        db.close()
        header = ["Course ID", "Course Title", "Description", "Instructor", "Total Students"]
        datas = []
        for result in results:
            curData = []
            curData.append(result[0])
            curData.append(result[1])
            curData.append(result[2])
            curData.append(result[3] if not result[3] == None else "No Instructor")
            curData.append(result[4])
            datas.append(curData)
        print(tabulate(datas, header, tablefmt="rounded_grid"))

    def addCourse(self):
        courseTitle = input("Enter Course Title: ")
        courseDescription = input("Enter Course Description: ")
        db.execute_query("INSERT INTO Course (courseTitle, courseDescription, totalStudents) VALUES (?,?,?)", (courseTitle, courseDescription, 0))
        db.close()

    def removeCourse(self, courseID):
        db.execute_query("DELETE FROM Course WHERE courseID = ?", (courseID))
        db.execute_query("DELETE FROM Schedule WHERE courseID = ?", (courseID))
        db.execute_query("DELETE FROM Module WHERE courseID = ?", (courseID))
        db.execute_query("DELETE FROM Enrollment WHERE courseID = ?", (courseID))
        db.execute_query("DELETE FROM Assignment WHERE courseID = ?", (courseID))
        db.close()

    def displayAllUsers(self, person): # 1 = students, 2 = instructors
        if person == "1":
            results = db.execute_query("SELECT * FROM Student")
            db.close()
            header = ["Student ID", "Name", "Email", "Gender", "Birth Date", "Address"]
            datas = []
            for result in results:
                curData = []
                curData.append(result[0])
                curData.append(result[3])
                curData.append(result[4])
                curData.append(result[5])
                curData.append(result[6])
                curData.append(result[7])
                datas.append(curData)
            print(tabulate(datas, header, tablefmt="rounded_grid"))
            return
        elif person == "2":
            results = db.execute_query("SELECT * FROM Instructor")
            db.close()
            header = ["Instructor ID", "Name", "Email", "Gender", "Birth Date", "Address"]
            datas = []
            for result in results:
                curData = []
                curData.append(result[0])
                curData.append(result[3])
                curData.append(result[4])
                curData.append(result[5])
                curData.append(result[6])
                curData.append(result[7])
                datas.append(curData)
            print(tabulate(datas, header, tablefmt="rounded_grid"))
            return
        else:
            print("INVALID CHOICE")

    def removeStudent(self, studentID):
        db.execute_query("DELETE FROM Student WHERE studentID = ?", (studentID))
        db.execute_query("DELETE FROM Enrollment WHERE studentID = ?", (studentID))
        db.close()

    def removeInstructor(self, instructorID):
        db.execute_query("DELETE FROM Instructor WHERE instructorID = ?", (instructorID))
        db.close()


