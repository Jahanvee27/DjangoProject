from django.http.response import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Question,Choice
from django.urls import reverse
from django.http import Http404


# Create your views here.

def index(request):
    return render(request, 'polls/index.html')

def first_page(request):
    latest_questions=Question.objects.order_by('-pub_date')[:5]
    template=loader.get_template('polls/first_page.html')
    response=template.render({'latest_questions':latest_questions})
    return HttpResponse(response)

def details(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exit")
    template=loader.get_template('polls/details.html')
    response=template.render({'question':question})
    return HttpResponse(response)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question,}) 

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.answer
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))








