class Question:
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer
    def checkanswer(self,answer):
        return self.answer==answer

class Quiz:
    def __init__(self,questions):
        self.questions=questions
        self.score=0
        self.questionsindex=0
    def getQuestion(self):
        return self.questions[self.questionsindex]
    def displayQuestion(self):
        question = self.getQuestion()
        print(f'Soru {self.questionsindex + 1}: {question.text}')

        for q in question.choices:
            print('-'+q)
        answer=input("Cevap:")
        self.guess(answer)
        self.loadQuestion()

    def guess(self,answer):
        question=self.getQuestion()

        if question.checkanswer(answer):
            self.score+=1
        self.questionsindex+=1

    def loadQuestion(self):
        if len(self.questions) == self.questionsindex:
            self.showscore()
        else:
            self.displayprogress()
            self.displayQuestion()
    def showscore(self):
        print("Score: ", self.score)

    def displayprogress(self):
        totalquestion = len(self.questions)
        questionnumber = self.questionsindex + 1

        if questionnumber > totalquestion:
            print("Quiz bitti.")
        else:
            print(f'Question {questionnumber} of {totalquestion}'.center(100,'*'))



q1=Question("En iyi programlama dili hangisidir?",['C#','python','java','javascript'],'python')
q2=Question("En popüler programlama dili hangisidir?",['C#','python','java','javascript'],'python')
q3=Question("En kazandıran programlama dili hangisidir?",['C#','python','java','javascript'],'python')
q4=Question("En sevilen programlama dili hangisidir?",['C#','python','java','javascript'],'python')
q5=Question("En kolay programlama dili hangisidir?",['C#','python','java','javascript'],'python')
questions=[q1,q2,q3,q4,q5]

quiz=Quiz(questions)
quiz.loadQuestion()

