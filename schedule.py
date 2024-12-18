from tabulate import tabulate
from enrollment import Enrollment

from database import Database
from config import DB_CONFIG

db = Database(**DB_CONFIG)

class Schedule:
    listOfSchedules = []

    def __init__(self, scheduleId, courseTitle, schedule, scheduleTitle):
        self.scheduleID = scheduleId
        self.courseTitle = courseTitle
        self. schedule = schedule
        self.scheduleTitle = scheduleTitle

    @classmethod
    def addToListOfSchedules(cls, records):
        for record in records:
            cls.listOfSchedules.append(Schedule(*record))

    
    @staticmethod
    def getSchedules():
        records = Enrollment.enrollmentRecords
        for record in records:
            result = db.execute_query("SELECT Schedule.scheduleID, Course.courseTitle, Schedule.schedule, Schedule.scheduleTitle FROM Schedule JOIN Course ON Course.courseID = Schedule.courseID WHERE Schedule.courseID = ?", (record.courseID))
            Schedule.addToListOfSchedules(result)
        db.close()
        

    @classmethod
    def displaySchedules(cls):
        Schedule.listOfSchedules = []
        Schedule.getSchedules()
        header = ["Course", "Schedule Title", "Schedule"]
        datas = []
        for schedule in cls.listOfSchedules:
            curData = []
            curData.append(schedule.courseTitle)
            curData.append(schedule.scheduleTitle)
            curData.append(schedule.schedule)
            datas.append(curData)
        print(tabulate(datas, header, tablefmt="rounded_grid"))


    @staticmethod
    def displayInstructedCourseSchedules(courseID):
        results = db.execute_query("SELECT Course.courseTitle, Schedule.scheduleTitle, Schedule.schedule FROM Schedule JOIN Course ON Course.courseID = Schedule.courseID WHERE Schedule.courseID = ?", (courseID))
        db.close()
        header = ["Course Title", "Schedule Title", "Schedule"]
        datas = []
        for result in results:
            curData = []
            curData.append(result[0])
            curData.append(result[1])
            curData.append(result[2])
            datas.append(curData)
        print(tabulate(datas, header, tablefmt="rounded_grid"))

    @staticmethod
    def addSchedule(courseID):
        scheduleTitle = input("Enter Schedule Title: ")
        schedule = input("Enter Schedule(YYYY-MM-DD HH:MM:SS): ")
        db.execute_query("INSERT INTO Schedule (courseID, schedule, scheduleTitle) VALUES (?,?,?)", (courseID, schedule, scheduleTitle))
        db.close()




