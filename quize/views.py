from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib.auth.views import logout

def main_page(request):
    return render(request, "quize/main_page.html")

def logout_page(request):
    logout(request)
    return HttpResponseRedirect("/")
