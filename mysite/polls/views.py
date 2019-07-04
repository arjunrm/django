# Create your views here.

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from django.template import loader

from .models import Question, Choice

def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    latest_question_list = Question.objects.all()

    # response as string
    # output = ', '.join(q.question_text for q in latest_question_list)
    # return HttpResponse(output)

    # response using html template
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list' : latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))

    # response using render
    context = {
        'latest_question_list' : latest_question_list,
    }
    return render(request, 'polls/index.html', context=context)

def detail(request, question_id):
    # return HttpResponse("You're looking at question %s" % question_id)

    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question' : question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question' : question})

def vote(request, question_id):
    print(request.POST)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # redisplay the question voting form
        return render(request, 'polls/detail.html', 
            {
                'question' : question,
                'error_message' : "You didn't select a choice!"
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# django's generic views

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.all()

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
