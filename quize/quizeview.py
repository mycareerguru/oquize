import datetime
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from quize.forms import RegisterForm, QuestionForm
from quize.models import Question, Tag, Answer, Quize, UserQuize

def quize_display(request , qid):
    q = Quize.objects.get(id=qid)
    uqs = UserQuize.objects.filter(quize=q, user=request.user).order_by("-start")[0:10];
    return render(request,"quize/quize_display.html",{
    'quize' : q,
    'uqs' : uqs,
    })

def quize_start(request , qid):
    q = Quize.objects.get(id=qid)
    uq = UserQuize(quize = q,
                   user = request.user,
                   start = datetime.datetime.now())
    uq.totalAttempted = 0;
    uq.totalCorrect = 0;
    uq.save();
    questions = q.questions.all()
    return render(request,"quize/quize_start.html",{
    'quize' : q,
    'uquize' : uq,
    'questions' : questions,
    'showTags' : False
    })