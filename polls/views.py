from django.shortcuts import render, get_object_or_404
from polls.models import Question


def index(request):
    question_list = Question.objects.all().order_by('-create_dt')
    return render(request, 'polls/index.html', {'question_list': question_list})


def detail(request, user_selected_question_id):
    question = get_object_or_404(Question, pk=user_selected_question_id)
    return render(request, 'polls/detail.html', {'question': question})
