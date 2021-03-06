import sys
import datetime
from django.contrib.auth.models import User
from quize.models import Question, Tag, Quize

class QuestionSaver():

    def __init__(self, username, tags):
        self.clear(username, tags)

    def clear(self, username, tags):
        self.questions = []
        self.user = User.objects.get(username=username)
        self.tags = []
        for tagname in tags:
            tag, dummy = Tag.objects.get_or_create(name=tagname)
            self.tags.append(tag)

    def saveQuestion(self, lines):
        q = Question(
            user=self.user,
            text=lines[0],
            opt1=lines[1],
            opt2=lines[2],
            opt3=lines[3],
            opt4=lines[4],
            ans=int(lines[5])
        )
        q.num_attemplted = 0
        q.num_correct = 0
        q.num_likes = 0
        q.num_unlikes = 0
        q.save()

        for tag in self.tags:
            q.tag_set.add(tag)
        q.save()
        self.questions.append(q);

    def readFile(self, filename):
        file = open(filename, 'r')
        count = 0
        q = []
        for line in file:
            q.append(line)
            count = count + 1
            if count == 6:
                self.saveQuestion(q)
                count = 0
                q = []

    def makeQuize(self, name, minutes):
        quiz = Quize()
        quiz.quizeName = name
        quiz.date_created = datetime.datetime.now()
        quiz.user = self.user
        quiz.timeAllowed = minutes
        quiz.totalQuestion = len(self.questions)
        quiz.save()
        for q in self.questions:
            quiz.questions.add(q)

        for tag in self.tags:
            quiz.tag_set.add(tag)
        quiz.save()

def add(name, filename, username, tags, minutes):
    qs = QuestionSaver(username, tags.split())
    qs.readFile(filename)
    qs.makeQuize(name, minutes)

def test():
    Question.objects.all().delete()
    add("math1", "questions/q1.txt", "sagar", "math general_apti",
        20)
    add("computerknowledge1", "questions/computer_knowledge1.txt",
        "sagar",
        "computerknowledge", 20)
    add("computerknowledge2", "questions/computer_knowledge2.txt",
        "sagar",
        "computerknowledge", 20)
    add("numberseries1", "questions/number_serise.txt",
        "sagar",
        "math numberseries", 30)
    add("Data_Structure 1", "questions/Data_Structure 1.txt",
        "sagar",
        "Data_Structure", 20)
    add("Data_Structure 2", "questions/Data_Structure 2.txt",
        "sagar",
        "Data_Structure", 20)
    add("Data-Structure 3", "questions/Data-Structure 3.txt",
        "sagar",
        "Data_Structure", 20)
    add("DBMS", "questions/DBMS.txt",
        "sagar",
        "DBMS", 20)
    add("DBMS 1", "questions/DBMS 1.txt",
        "sagar",
        "DBMS", 20)
    add("DBMS (2)", "questions/DBMS (2).txt",
        "sagar",
        "DBMS", 20)
    add("DBMS (3)", "questions/DBMS (3).txt",
        "sagar",
        "DBMS", 20)
    add("gk_test", "questions/gk_test.txt",
        "sagar",
        "Genral knowledge", 20)
    add("Mental Ability", "questions/Mental Ability.txt",
        "sagar",
        "Mental Ability", 20)
    add("Mental Ability 1", "questions/Mental Ability 1.txt",
        "sagar",
        "Mental Ability", 20)
    add("Operating System", "questions/Operating System.txt",
        "sagar",
        "Operating System", 20)
    add("Networking", "questions/Networking.txt",
        "sagar",
        "Networking", 20)
    add("Networking (2)", "questions/Networking (2).txt",
        "sagar",
        "Networking", 20)
    
def main():
        filename = sys.argv[1]
        username = sys.argv[2]
        tags = sys.argv[3]
        q = QuestionSaver(username, tags.split())
        q.readFile(filename, username)

if __name__ == "__main__":
    main()
