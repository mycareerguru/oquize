from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from quize.forms import RegisterForm, QuestionForm
from quize.models import Question, Tag, Answer, Quize, UserQuize, QuizeAnswers
from quize.models import UserQuestion

def main_page(request):
    return render(request, "quize/main_page.html")

@login_required
def user_page(request, user):
    questions = Question.objects.all().order_by('-date_added')

    return render(request, "quize/user_page.html", {
        'questions' : questions,
        'showTags' : True,
        'showLikes' : True,
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
    q=a.quizes.all();
    return render(request,"quize/tag_display.html",{
    'questions' : b,
    'quizes' : q,
    'showTags' : False,
    'showLikes' : True,
    })
    
def search_page(request):
    questions = []
    showResult = False
    query = ""
    qlist = []
    quizes = []
    if 'query' in request.GET:
        query = request.GET['query']
        showResult = True;
        questions =Question.objects.filter(text__icontains=query)[:50]
        qlist = list(questions)
        tags = Tag.objects.filter(name__icontains=query)
        for tag in tags:
            q = tag.questions.all()[:50]
            qlist.extend(list(q))
            
        for tag in tags:
            qz = tag.quizes.all()[:50]
            quizes.extend(list(qz))
    qlist=set(qlist)
    return render(request, "quize/searchcombine.html", {
        'questions' : qlist,
        'quizes' : quizes,
        'showResult' : showResult,
        'query' : query,
        'showLikes' : True,
    })

def save_general_ans(request, question, user_ans):
    try:
        answer = Answer.objects.get(user=request.user, question=question)
    except:
        answer = Answer(user=request.user, question=question, ans=user_ans)
        
    answer.ans = user_ans
    answer.correct = (question.ans == user_ans);  
    answer.num_attemps = answer.num_attemps + 1    
    answer.save()
    
    
def save_quize_ans(request, question, user_ans, quizeid):
    created = False
    quiz = UserQuize.objects.get(id=quizeid)
    try:
        answer = QuizeAnswers.objects.get(
            quize=quiz,
            question=question,
        )
        created = False;
    except:
        answer = QuizeAnswers(
            quize=quiz,
            question=question,
        )
        created = True;
    answer.ans = user_ans
    answer.correct = (question.ans == user_ans);  
    answer.num_attemps = answer.num_attemps + 1
    answer.save()
    
    if (answer.correct):
        quiz.totalCorrect = quiz.totalCorrect + 1
    if created:
        quiz.totalAttempted = quiz.totalAttempted + 1
        
    quiz.save()    
    
    
@login_required
def user_answer(request):
    if not request.method == "GET":
        raise Http404

    user_ans = int(request.GET['ans'])
    user_q = request.GET['question']
    quizeid = request.GET['qid'];
    question = Question.objects.get(id=user_q)
    print "Submitting answer question " + str(user_q) + "quize " + str(quizeid)
    
    if int(quizeid) == 0:
        save_general_ans(request, question, user_ans)
    else:
        save_quize_ans(request, question, user_ans, quizeid)
        
    return HttpResponse("Hello")    
        
    
   
@login_required
def quiz_page(request):
    # TODO limit size of rows and order by data created
    # quizes = Quize.objects.all().order_by("-date_created")[0:50]
    quizes = Quize.objects.all()
    return render(request, "quize/quize_page.html", {
        'quizes' : quizes,
    })


@login_required
def like_page(request):
    id = request.GET['id']
    q = Question.objects.get(id=id)
    uq, created = UserQuestion.objects.get_or_create(user=request.user, question=q)
    if not (uq.liked or uq.unliked):
        uq.liked = True
        uq.save()
        q.num_likes  = q.num_likes + 1
        q.save()
    return HttpResponse(str(q.num_likes))

        
@login_required
def unlike_page(request):
    id = request.GET['id']
    q = Question.objects.get(id=id)
    uq, created = UserQuestion.objects.get_or_create(user=request.user, question=q)
    if not (uq.liked or uq.unliked):
        uq.unliked = True
        uq.save()
        q.num_unlikes  = q.num_unlikes + 1
        q.save()
    return HttpResponse(str(q.num_unlikes))


def close_page(request):
    id = request.GET['id']
    q = Question.objects.get(id=id)
    uq, created = UserQuestion.objects.get_or_create(
        user=request.user, question=q)
    uq.closed = True
    uq.save()
    return HttpResponse("ok")


def question_page(request, id):
    q = Question.objects.get(id=id)
    return render(request, "quize/question_page.html", {
            'q' : q
            });
