from django.views.generic import DetailView, ListView

from app.models import Submission, User


class UserProfileView(DetailView):
    template_name = 'profile.html'
    model = User
    context_object_name = 'profile'

    slug_field = 'username'
    slug_url_kwarg = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        ac_submissions = Submission.objects.filter(user=self.object, status='AC')
        context['num_problems_solved'] = ac_submissions.values('problem').distinct().count()

        return context


class UserListView(ListView):
    template_name = 'users.html'
    model = User
    context_object_name = 'users'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        for user in context['users']:
            ac_submissions = Submission.objects.filter(user=user, status='AC')
            user.num_problems_solved = ac_submissions.values('problem').distinct().count()

        context['users'] = sorted(context['users'], key=lambda user: -user.num_problems_solved)

        return context
