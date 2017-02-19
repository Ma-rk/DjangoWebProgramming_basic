from django.shortcuts import render, get_object_or_404
from polls.models import Question, Answer
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def index(request):
    question_list = Question.objects.all().order_by('-create_dt')
    return render(request, 'polls/index.html', {'question_list': question_list})


def detail(request, user_selected_question_id):
    question = get_object_or_404(Question, pk=user_selected_question_id)
    return render(request, 'polls/detail.html', {'question': question})


def vote(request, user_selected_question_id):
    question = get_object_or_404(Question, pk=user_selected_question_id)
    try:
        user_selected_answer = question.answer_set.get(pk=request.POST['answer'])
    except (KeyError, Answer.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'err_msg': "You didn't select an answer."
        })
    else:
        user_selected_answer.num_of_votes += 1
        user_selected_answer.save()
        return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))


def result(request, user_selected_question_id):
    question = get_object_or_404(Question, pk=user_selected_question_id)
    return render(request, 'polls/result.html', {'question': question})
