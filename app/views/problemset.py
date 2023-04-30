from django.views.generic import DetailView, ListView

from app.models import Problem, ProblemCategory, Submission


class ProblemsetView(ListView):
    template_name = 'problemset.html'
    context_object_name = 'problemset'

    slug_field = 'code'
    slug_url_kwarg = 'problemset'

    ordering = ['id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            submissions = Submission.objects.filter(user=self.request.user)
            ac_submissions = submissions.filter(status='AC')

            for problem in context['problemset']:
                problem.submitted = submissions.filter(problem=problem).exists()
                problem.solved = ac_submissions.filter(problem=problem).exists()

        context['problem_category'] = ProblemCategory.objects.get(code=self.kwargs['problemset'])

        return context

    def get_queryset(self):
        return Problem.objects.filter(category__code=self.kwargs['problemset'])


class ProblemCategoryView(ListView):
    template_name = 'problemsets.html'
    model = ProblemCategory
    context_object_name = 'problem_categories'

    ordering = ['id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            ac_submissions = Submission.objects.filter(user=self.request.user, status='AC')

            for category in context['problem_categories']:
                category.num_problems = Problem.objects.filter(category=category).count()
                category.num_solved = ac_submissions.filter(problem__category=category) \
                                                    .values('problem').distinct().count()
        else:
            for category in context['problem_categories']:
                category.num_problems = category.num_solved = 0

        return context
