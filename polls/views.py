from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Question, Choice

def index(request):

    questions = Question.objects.all()
    context = {
        'title' : 'polls',
        'questions' : questions
    }
    # return HttpResponse('hello manager of POlls')

    return render(request, 'polls/index.html', context) 


def details(request, id=None):
    
    question = Question.objects.get(id=id)
    created_by = question.created_by.first_name or None

    context = {
        'question' : question,
        'created_by' : created_by
    }

    return render(request, 'polls/details.html', context)