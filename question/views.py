from django.shortcuts import render

from .models import Question



def question_list(request):
    data = Question.objects.all()
    



























#def add_question(request):
    


