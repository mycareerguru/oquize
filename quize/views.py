from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib.auth.views import logout
from django.contrib.auth.models import User
from quize.forms import RegisterForm, QuestionForm
from quize.models import Question, Tag

def main_page(request):
    return render(request, "quize/main_page.html")

def user_page(request, user):
    questions = Question.objects.all()
    return render(request, "quize/user_page.html", {
        'questions' : questions
    })
    
def add_question(request):
    form = QuestionForm()
    
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            q = Question(
                text = form.cleaned_data['text'],
                opt1 = form.cleaned_data['opt1'],
                opt2 = form.cleaned_data['opt2'],
                opt3 = form.cleaned_data['opt3'],
                opt4 = form.cleaned_data['opt4'],
                user=request.user,
                ans=form.cleaned_data['ans']
            )
            q.num_attemplted = 0
            q.num_correct = 0
            q.num_likes = 0
            q.num_unlikes = 0
            tags = form.cleaned_data['tags']
            for t in tags.split():
                tag, dummy = Tag.objects.get_or_create(name=t)
                q.tag_set.add(tag)
                
            q.save()
            
    return render(request, "quize/add_question.html", {
        'form' : form
    })
    
