from question import Question

from database import Database
from config import DB_CONFIG

db = Database(**DB_CONFIG)

class Quiz:
  def __init__(self, quizID, moduleID, totalItems, passingScore):
    self.quizID = quizID
    self.moduleID = moduleID
    self.totalItems = totalItems
    self.passingScore = passingScore

  @staticmethod
  def getQuestions(quizID):
    query = "SELECT * FROM Question WHERE quizID = ?"
    params = (quizID)
    questions = db.execute_query(query, params)
    return questions

  @staticmethod
  def doQuiz(moduleID):
    score = 0
    query = "SELECT * FROM Quiz WHERE moduleID = ?"
    params = (moduleID)
    quiz = db.execute_query(query, params, False)
    db.close()
    questions = Quiz.getQuestions(quiz[0]) #* HERE
    print(f"QUIZ / Total Items: {quiz[2]} / Passing Score: {quiz[3]}")
    number = 1
    for question in questions:
      print(f"{number}. {question[2]}")
      number += 1
      answer = input("Enter your Answer: ")
      if answer == question[3]:
        score += 1
    print("Your Score:", score)
    return True if score >= quiz[3] else False
  
  @staticmethod
  def getQuizCount(moduleID):
    count = db.execute_query("SELECT COUNT(*) FROM Quiz WHERE moduleID = ?", (moduleID), False)
    db.close()
    return count[0]
  
  @staticmethod
  def createQuiz(moduleID):
    totalItems = int(input("Enter Total Items: "))
    passingScore = int(input("Enter Passing Score: "))
    query = "INSERT INTO Quiz (moduleID, totalItems, passingScore) OUTPUT INSERTED.* VALUES (?,?,?)"
    params = (moduleID, totalItems, passingScore)
    result = db.execute_query(query, params, False)
    db.connection.commit()
    db.close()
    quizID = result[0]
    print("QUIZ ID:", quizID)

    for i in range(totalItems):
      question = input(f"Enter Question #{i + 1}: ")
      answer = input(f"Enter Answer: ")
      print("INSERTING QUESTION...")
      Question.createQuestion(quizID, question, answer)

    
    




    

  