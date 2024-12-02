from database import Database
from config import DB_CONFIG

db = Database(**DB_CONFIG)

class Question:

    @staticmethod
    def createQuestion(quizID, question, answer):
        db.execute_query("INSERT INTO Question (quizID, question, answer) VALUES (?,?,?)", (quizID, question, answer))
        db.close()
    
    @staticmethod
    def createQuestions(quizID, totalItems):
        for i in range(totalItems):
            question = input(f"Enter Question #{i + 1}: ")
            answer = input(f"Enter Answer: ")
            print("QUIZ ID:", quizID)
            print("INSERTING INTO QUESTION...")
            db.execute_query("INSERT INTO Question (quizID, question, answer) VALUES (?,?,?)", (quizID, question, answer))
        db.close()