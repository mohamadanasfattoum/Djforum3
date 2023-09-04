from django.shortcuts import render

from .models import Question



def question_list(request):
    data = Question.objects.all()
    return render(request, 'question_list.html',{'question':data})




























#def add_question(request):
    


