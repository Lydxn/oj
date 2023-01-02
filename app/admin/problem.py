from django.contrib.admin import ModelAdmin
from django.db import models

from app.widgets import CustomAdminMartorWidget

from app.models import Problem

class ProblemAdmin(ModelAdmin):
    fields = ('name', 'slug', 'category', 'tags', 'time_limit', 'memory_limit', 'statement')
    formfield_overrides = {
        models.TextField: {'widget': CustomAdminMartorWidget}
    }
