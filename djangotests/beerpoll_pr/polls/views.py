# -*- coding: cp1252 -*-

# Create your views here.

from django.http import HttpResponse
from django.http import Http404
#from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ',<br/>'.join([q.question_text for q in latest_question_list])
    #return HttpResponse("Index des questions : <br/>"+output)
    
    #template = loader.get_template('polls/index.html')
    #context = {
    #    'latest_question_list': latest_question_list,
    #}
    #return HttpResponse(template.render(context, request))
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    #return HttpResponse("Ceci est la question %s." % question_id)
    
    #try:
    #    question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #    raise Http404("La question demandee, numero " + question_id + " n'existe pas.")
    #return render(request, 'polls/detail.html', {'question': question})

    question = get_object_or_404(Question,pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def vote(request, question_id):
    return HttpResponse("Vous votez pour la question %s." % question_id)

def results(request, question_id):
    return HttpResponse("Resultats pour la question %s." % question_id)

