from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin

from algogym import settings
from app.forms import SubmissionForm
from app.models import Problem, Submission, SubmissionCase

import threading


def get_recent_submission(user, problem):
    if user.is_authenticated:
        try:
            return Submission.objects.filter(user=user, problem=problem) \
                                     .latest('submitted')
        except Submission.DoesNotExist:
            pass

    return None


class ProblemDetailView(FormMixin, DetailView):
    template_name = 'problem.html'
    model = Problem
    form_class = SubmissionForm
    context_object_name = 'problem'
    
    slug_field = 'code'
    slug_url_kwarg = 'problem'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.recent_submission:
            context['submission'] = self.recent_submission
            context['test_cases'] = SubmissionCase.objects.filter(submission=self.recent_submission)

        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        if self.request.user.is_authenticated:
            kwargs['instance'] = Submission(
                user=self.request.user, problem=self.object
            )
        if self.recent_submission:
            kwargs['initial'] = {
                'language': self.recent_submission.language,
                'source': self.recent_submission.source
            }

        return kwargs

    def form_valid(self, form):
        submission = form.save()

        # Perform the judging in the background and poll for status using AJAX.
        threading.Thread(target=submission.judge, daemon=True).start()

        return HttpResponseRedirect(self.request.path_info)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.recent_submission = get_recent_submission(self.request.user, self.object)

        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # TODO: AJAX, Codemirror highlighting for other languages

        self.object = self.get_object()
        self.recent_submission = get_recent_submission(self.request.user, self.object)

        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class SubmissionView(DetailView):
    template_name = 'submission.html'
    model = Submission

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['submission'] = self.object
        context['test_cases'] = SubmissionCase.objects.filter(submission=self.object)

        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        return super().get(request, *args, **kwargs)
