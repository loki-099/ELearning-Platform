from database import Database
from config import DB_CONFIG

db = Database(**DB_CONFIG)

class Question:

    @staticmethod
    def createQuestion(quizID, question, answer):
        db.execute_query("INSERT INTO Question (quizID, question, answer) VALUES (?,?,?)", (quizID, question, answer))
        db.close()
    