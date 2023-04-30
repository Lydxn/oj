from django.contrib.admin import ModelAdmin
from django.db import models

from app.models import Problem
from app.widgets import CustomAdminMartorWidget


class ProblemAdmin(ModelAdmin):
    fields = ('name', 'code', 'category', 'difficulty', 'time_limit', 'memory_limit', 'statement')
    formfield_overrides = {
        models.TextField: {'widget': CustomAdminMartorWidget}
    }
