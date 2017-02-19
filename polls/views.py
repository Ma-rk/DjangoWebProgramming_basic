from django.shortcuts import render
from polls.models import Question


def index(request):
    question_list = Question.objects.all().order_by('-create_dt')
    return render(request, 'polls/index.html', {'question_list': question_list})
