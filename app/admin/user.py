from django.contrib.admin import ModelAdmin

from app.widgets import CustomAdminMartorWidget

from app.models import User

class UserAdmin(ModelAdmin):
    fields = ('username', 'password', 'email', 'date_joined', 'last_login',
              'is_superuser', 'is_staff', 'is_active')
