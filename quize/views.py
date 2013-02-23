from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib.auth.views import logout
from django.contrib.auth.models import User
from quize.forms import RegisterForm
from quize.models import Question

def main_page(request):
    return render(request, "quize/main_page.html")

def user_page(request, user):
    questions = Question.objects.all()
    return render(request, "quize/user_page.html", {
        'questions' : questions
    })
    
