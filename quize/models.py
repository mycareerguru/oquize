import datetime
from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    date_added = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User)
    text = models.TextField()
    opt1 = models.TextField()
    opt2 = models.TextField()
    opt3 = models.TextField()
    opt4 = models.TextField()
    ans = models.IntegerField()
    num_attemplted = models.IntegerField(default=0)
    num_correct = models.IntegerField(default=0)
    num_likes = models.IntegerField(default=0)
    num_unlikes = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.user.username + self.text + self.date_added.__str__()

class Answer(models.Model):
    question = models.ForeignKey(Question)
    user = models.ForeignKey(User)
    ans = models.IntegerField()
    correct = models.BooleanField(default=False)
    num_attemps = models.IntegerField(default=0)
    
    def __unicode__(self):
        return str(self.question.id) + " " + self.user.username + " " + str(self.ans) + " attemps " + str(self.num_attemps) + " " + str(self.correct)

class Quize(models.Model):
    quizeName = models.CharField(max_length=30)
    totalQuestion = models.IntegerField()
    timeAllowed = models.IntegerField()
    date_created = models.DateTimeField()
    user = models.ForeignKey(User)
    questions = models.ManyToManyField(Question)

    def __unicode__(self):
        return self.quizeName
    
class UserQuize(models.Model):
    user = models.ForeignKey(User)
    quize = models.ForeignKey(Quize)
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(blank=True, null=True)
    totalAttempted = models.IntegerField(default=0)
    totalCorrect = models.IntegerField(default=0)

    def __unicode__(self):
        return "[" + str(self.id) + " " + self.user.username + " " + self.quize.quizeName + "]"
    
class QuizeAnswers(models.Model):
    quize = models.ForeignKey(UserQuize)
    question = models.ForeignKey(Question)
    ans = models.IntegerField()
    correct = models.BooleanField(default=False)
    num_attemps = models.IntegerField(default=0)
    
    def __unicode__(self):
        retstr = "[" + str(self.id) + " " + self.question.text
        retstr += " " + str(self.ans) + "]"
        return retstr
 
class Tag(models.Model):
    name = models.CharField(max_length=30,unique=True)
    questions = models.ManyToManyField(Question)
    quizes = models.ManyToManyField(Quize)
    def __unicode__(self):
        return self.name


class UserQuestion(models.Model):
    question = models.ForeignKey(Question)
    user = models.ForeignKey(User)
    liked = models.BooleanField(default=False)
    unliked = models.BooleanField(default=False)
    answered = models.BooleanField(default=False)
    closed = models.BooleanField(default=False)
