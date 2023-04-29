from django.shortcuts import render
from django.views.generic import DetailView


class IndexView(DetailView):
    def get(self, request):
        return render(request, 'index.html')
