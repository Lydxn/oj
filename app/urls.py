from django.contrib import admin
from django.urls import path

from app.views.index import IndexView
from app.views.misc import AboutView
from app.views.problem import ProblemDetailView, SubmissionView
from app.views.problemset import ProblemSetView
from app.views.user import UserListView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('problem/<str:code>/', ProblemDetailView.as_view(), name='problem'),
    path('problemset/', ProblemSetView.as_view(), name='problemset'),
    path('submission/<int:pk>/', SubmissionView.as_view(), name='submission'),
    path('users/', UserListView.as_view(), name='users')
]
