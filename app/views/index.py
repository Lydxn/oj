from django.shortcuts import render
from django.views.generic import TemplateView

from app.models.submission import Submission

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['recent_submissions'] = Submission.objects.order_by('-submitted')[:20]

        return context
