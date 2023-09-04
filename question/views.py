from django.shortcuts import render

from .models import Question



def question_list(request):
    data = Question.objects.all()
    return render(request, 'question_list.html',{'question':data})




def question_detail(request,question_id):
    data = Question.objects.git(id=question_id)
    return render(request, 'question_detail.html',{'question':data})






















#def add_question(request):
    


