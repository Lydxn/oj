from django.views.generic import DetailView, ListView

from app.models import Problem, Submission


class ProblemSetView(ListView):
    template_name = 'problemset.html'

    model = Problem
    context_object_name = 'problemset'

    ordering = ['id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        submissions = Submission.objects.filter(user=self.request.user)
        ac_submissions = submissions.filter(status='AC')

        for problem in context['problemset']:
            problem.submitted = submissions.filter(problem=problem).exists()
            problem.solved = ac_submissions.filter(problem=problem).exists()

        return context
