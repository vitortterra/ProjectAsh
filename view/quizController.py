from flask import Flask, render_template, request, redirect
from mockServices import getThemes, getUserID, getQuiz, Quiz, getResult, Result

app = Flask(__name__)

@app.route('/')
def home():
   homeTitle = "Bem-vindo!"
   homeText = "Escolha uma matéria para aprender"
   themes = getThemes()
   sortedThemeKeys = sorted(themes.keys())
   entries = [homeTitle, homeText, [(k, themes[k]) for k in sortedThemeKeys]]
   return render_template('home.html', entries=entries)

@app.route('/lesson', methods=['POST'])
def about():
    themeID = request.form['themeID']
    userID = getUserID()
    quiz = getQuiz(userID, themeID)
    sortedQuizKeys = sorted(quiz.alternatives.keys())
    entries = [quiz.lessonContent, quiz.questionContent] + [quiz.alternatives[k] for k in sortedQuizKeys]
    entries.append(quiz.correctAlternative)
    entries.append(quiz.quizID)
    entries.append(themeID)
    return render_template('lesson.html', entries=entries)

@app.route('/result', methods=['POST'])
def result():
    chosenAlternative = request.form['alternative']
    correctAlternative = request.form['correctAlternative']
    quizID = request.form['quizID']
    themeID = request.form['themeID']
    isCorrect = chosenAlternative == correctAlternative
    result = getResult(quizID, chosenAlternative, isCorrect)
    entries = [result.message, result.willContinue, themeID]
    #return redirect('/')
    return render_template('result.html', entries=entries)
    	
if __name__ == '__main__':
    app.run(debug=True)
