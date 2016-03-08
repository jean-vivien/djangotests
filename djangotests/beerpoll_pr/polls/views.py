from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ',<br/>'.join([q.question_text for q in latest_question_list])
    return HttpResponse("Index des questions : <br/>"+output)

def detail(request, question_id):
    return HttpResponse("Ceci est la question %s." % question_id)

def vote(request, question_id):
    return HttpResponse("Vous votez pour la question %s." % question_id)

def results(request, question_id):
    return HttpResponse("Resultats pour la question %s." % question_id)

