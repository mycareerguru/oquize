from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from quize.forms import RegisterForm, QuestionForm
from quize.models import Question, Tag, Answer, Quize, UserQuize, QuizeAnswers
from quize.models import UserQuestion


@login_required
def result_page(request):
    try:
        answers = Answer.objects.filter(user=request.user)
    except:
        return Http404
    total_correct = 0
    total_wrong = 0
    total_attempts = 0
    for ans in answers:
        total_attempts = total_attempts + ans.num_attemps
        if ans.correct:
            total_correct = total_correct + 1
        else:
            total_wrong = total_wrong + 1
    return render(request, "quize/result_page.html", {
        'total_attempts' : total_attempts,
        'total_correct' : total_correct,
        'total_wrong' : total_wrong,
        'answers' : answers,
    })
 
