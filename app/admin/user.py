from django.contrib.admin import ModelAdmin

from app.models import User
from app.widgets import CustomAdminMartorWidget


class UserAdmin(ModelAdmin):
    fields = ('username', 'password', 'email', 'date_joined', 'last_login',
              'is_superuser', 'is_staff', 'is_active')
