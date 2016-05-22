def getThemes():
	'''
	rtype: {themeID (str) : themeName (str)}
	'''
	return {"TID1" : "Assunto 1", "TID2" : "Assunto 2", "TID3" : "Assunto 3"}

def getUserID():
	'''
	rtype: str
	'''
	return "user1"

def getQuiz(userID, themeID):
	'''
	rtype: Quiz
	'''
	mockQuiz = Quiz("mockid",
					"Leia aqui sobre o Teorema de Pitágoras",
					"A soma dos quadrados dos catetos é igual ao quadrado da",
					{"a" : "hipotenusa",
					 "b" : "hipertenusa",
					 "c" : "hipopótama",
					 "d" : "ortotenusa",
					 "e" : "medusa"},
					 "a",
					userID)
	return mockQuiz

def getResult(quizID, chosenAlternative, isCorrect):
	mockResult = Result("Mensagem de feedback para o aluno", False)
	return mockResult

class Quiz:
	'''
	quizID: str
	lessonContent: str
	questionContent: str
	alternatives: {str:str}
	correctAlternative: str
	userID: str
	'''
	def __init__(self, quizID, lessonContent, questionContent, alternatives, correctAlternative, userID):
		self.quizID = quizID
		self.lessonContent = lessonContent
		self.questionContent = questionContent
		self.alternatives = alternatives
		self.correctAlternative = correctAlternative
		self.userID = userID

class Result:
	'''
	message: str
	willContinue: bool
	'''
	def __init__(self, message, willContinue):
		self.message = message
		self.willContinue = willContinue

