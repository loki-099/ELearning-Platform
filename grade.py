from tabulate import tabulate
from enrollment import Enrollment

from database import Database
from config import DB_CONFIG

db = Database(**DB_CONFIG)

class Grade:

    @staticmethod
    def gradeStatus(grade):
        return "No Grade" if grade == 0 else grade
    
    @staticmethod
    def displayGrades():
        records = Enrollment.enrollmentRecords
        header = ["Course", "Grade"]
        datas = []
        for record in records:
            curData = []
            curData.append(Enrollment.getCourseTitle(record.courseID))
            curData.append(Grade.gradeStatus(record.grade))
            datas.append(curData)
        print(tabulate(datas, headers=header, tablefmt="rounded_grid"))

    @staticmethod
    def giveGrade(courseID, studentID):
        grade = int(input("Enter Grade to Give: "))
        db.execute_query("UPDATE Enrollment SET grade = ? WHERE courseID = ? AND studentID = ?", (grade, courseID, studentID))
        db.close()

