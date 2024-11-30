from tabulate import tabulate
from enrollment import Enrollment

from database import Database
from config import DB_CONFIG

db = Database(**DB_CONFIG)

class Grade:
    
    @staticmethod
    def displayGrades():
        records = Enrollment.enrollmentRecords
        header = ["Course", "Grade"]
        datas = []
        for record in records:
            curData = []
            curData.append(Enrollment.getCourseTitle(record.courseID))
            curData.append(record.grade)
            datas.append(curData)
        print(tabulate(datas, headers=header, tablefmt="rounded_grid"))
