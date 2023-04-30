from django.contrib import admin
from django.urls import path

from app.views.index import IndexView
from app.views.misc import AboutView
from app.views.problem import ProblemDetailView, SubmissionView
from app.views.problemset import ProblemCategoryView, ProblemsetView
from app.views.user import UserView, UserListView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('problem/<str:problem>/', ProblemDetailView.as_view(), name='problem'),
    path('problemset/<str:problemset>', ProblemsetView.as_view(), name='problemset'),
    path('problemsets/', ProblemCategoryView.as_view(), name='problemsets'),
    path('submission/<int:pk>/', SubmissionView.as_view(), name='submission'),
    path('user/<str:user>', UserView.as_view(), name='user'),
    path('users/', UserListView.as_view(), name='users')
]
