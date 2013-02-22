from django.http import HttpResponse
from django.shortcuts import render, render_to_response

def main_page(request):
    return render_to_response("quize/main_page.html")
    
