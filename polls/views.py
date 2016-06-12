from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import View

from .models import Choice, Question


class IndexView(View):
    template_name = 'polls/index.html'

    def get(self, request, *args, **kwargs):
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        context = {
            'latest_question_list': latest_question_list,
        }
        return render(request, self.template_name, context)


class DetailView(View):
    template_name = 'polls/detail.html'

    def get(self, request, *args, **kwargs):
        question = get_object_or_404(Question, pk=kwargs['pk'])
        return render(request, self.template_name, {'question': question})


class ResultsView(DetailView):
    template_name = 'polls/results.html'


class VoteView(View):
    template_name = 'polls/detail.html'

    def post(self, request, *args, **kwargs):
        question = get_object_or_404(Question, pk=kwargs['question_id'])
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            # Redisplay the question voting form.
            return render(request, self.template_name, {
                'question': question,
                'error_message': "You didn't select a choice.",
            })
        else:
            selected_choice.votes += 1
            selected_choice.save()
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))