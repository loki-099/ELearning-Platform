from tabulate import tabulate
from database import Database
from config import DB_CONFIG

from enrollment import Enrollment

db = Database(**DB_CONFIG)

class Assignment:

    @staticmethod
    def getAssignmentDetails(enrollmentID):
        query = "SELECT Enrollment.enrollmentID, Course.courseTitle, Assignment.assignmentTitle, Assignment.dueDate, Enrollment.assignmentStatus FROM Enrollment JOIN Assignment ON Enrollment.assignmentID = Assignment.assignmentID JOIN Course ON Course.courseID = Assignment.courseID WHERE enrollmentID = ?"
        params = (enrollmentID)
        result = db.execute_query(query, params, False)
        db.close()
        return result

    
    #* COURSE TITLE | ASSIGNMENT TITLE | DUE DATE | STATUS
    @staticmethod
    def displayAssignments(studentID):
        records = Enrollment.getEnrollmentRecordByStudentID(studentID)
        headers = ["Number", "Course Title", "Assignment Title", "Due Date", "Status"]
        datas = []
        for record in records:
            curData = []
            details = Assignment.getAssignmentDetails(record[0])
            curData.append(details[0])
            curData.append(details[1])
            curData.append(details[2])
            curData.append(details[3])
            curData.append(details[4])
            datas.append(curData)
        print(tabulate(datas, headers=headers, tablefmt="rounded_grid"))

    @staticmethod
    def submitAssignment(enrollmentID):
        query = "UPDATE Enrollment SET assignmentStatus = ? WHERE enrollmentID = ?"
        params = ("Submitted", enrollmentID)
        db.execute_query(query, params)
        db.close()


    @staticmethod
    def displayAssignmentStatus(courseID):
        print("")
        results = db.execute_query("SELECT Student.fullName, Course.courseTitle, Assignment.assignmentTitle, Enrollment.assignmentStatus FROM Enrollment JOIN Student ON Student.studentID = Enrollment.studentID JOIN Course ON Course.courseID = Enrollment.courseID JOIN Assignment ON Assignment.assignmentID = Enrollment.assignmentID WHERE Enrollment.courseID = ?", (courseID))
        header = ["Student Name", "Course Title", "Assignment Title", "Status"]
        datas = []
        for result in results:
            curData = []
            curData.append(result[0])
            curData.append(result[1])
            curData.append(result[2])
            curData.append(result[3])
            datas.append(curData)
        print(tabulate(datas, header, tablefmt="rounded_grid"))

            
        
