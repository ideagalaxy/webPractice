from django.http import HttpResponse
from .models import *
from django.shortcuts import render


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'first_question' : latest_question_list[0]}
    #output = ", ".join([q.quesiton_text for q in latest_question_list])
    #print(output)

    return render(request, 'appname/index.html',context)


def some_url(request):
    return HttpResponse("SomeUrl을 구현해 봤습니다!!")