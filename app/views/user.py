from django.views.generic import ListView

from app.models import User


class UserListView(ListView):
    template_name = 'users.html'

    model = User
    context_object_name = 'users'
