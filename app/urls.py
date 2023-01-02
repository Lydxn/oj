from django.contrib import admin
from django.urls import path

from app.views.index import IndexView
from app.views.problem import ProblemView, ProblemSetView
from app.views.user import UserListView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('problem/<slug:slug>/', ProblemView.as_view(), name='problem'),
    path('problemset/', ProblemSetView.as_view(), name='problemset'),
    path('users/', UserListView.as_view(), name='users')
]
