from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from quize.forms import RegisterForm, QuestionForm
from quize.models import Question, Tag

def main_page(request):
    return render(request, "quize/main_page.html")

@login_required
def user_page(request, user):
    questions = Question.objects.all()
    return render(request, "quize/user_page.html", {
        'questions' : questions
    })

    
@login_required
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
            q.save()
            tags = form.cleaned_data['tags']
            for t in tags.split():
                tag, dummy = Tag.objects.get_or_create(name=t)
                q.tag_set.add(tag)
                
            q.save()
            return HttpResponseRedirect("/")
            
    return render(request, "quize/add_question.html", {
        'form' : form
    })

    
def tag_page(request):
    tags = Tag.objects.all()
    return render(request, "quize/tag.html",{
    'tags' : tags
    })
    
    
def tag_display(request , tag):
    a=Tag.objects.get(name = tag)
    b=a.questions.all()
    return render(request,"quize/tag_display.html",{
    'questions' : b
    })
    
def search_page(request):
    questions = []
    showResult = False
    query = ""
    qlist = []
    if 'query' in request.GET:
        query = request.GET['query']
        showResult = True;
        questions = Question.objects.filter(text__icontains=query)[:10]
        qlist = list(questions)
        tags = Tag.objects.filter(name__icontains=query)
        for tag in tags:
            q = tag.questions.all()[:10]
            qlist.extend(list(q))
            
    return render(request, "quize/search.html", {
        'questions' : qlist,
        'showResult' : showResult,
        'query' : query
    })
    
