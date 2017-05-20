from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import RequestContext, loader

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list':latest_question_list}
    return render(request,'polls/index.html',context)
def detail(request,question_id):
    return HttpResponse("You're locking at question %s." % question_id)
def result(request,question_id):
    response = "You're locking at the resultsof question %s."
    return  HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("You're voting on  qustion %s ." % question_id)