from django.shortcuts import render
from .models import Question
from .forms import QuestionForm



def question_list(request):
    data = Question.objects.all()
    return render(request, 'question_list.html',{'question':data})




def question_detail(request,question_id):
    data = Question.objects.get(id=question_id)
    return render(request, 'question_detail.html',{'question':data})


def add_question(request):
    form = QuestionForm.objects.get(id=question_id)
    return render(request, 'add_question.html',{'form':form})





















#def add_question(request):
    


