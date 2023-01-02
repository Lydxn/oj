from django.views.generic import DetailView, ListView

from app.models import Problem

class ProblemView(DetailView):
    model = Problem
    template_name = 'problem.html'
    context_object_name = 'problem'

class ProblemSetView(ListView):
    model = Problem
    template_name = 'problemset.html'
    context_object_name = 'problemset'

    ordering = ['id']
