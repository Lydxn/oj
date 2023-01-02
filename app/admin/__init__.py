from django.contrib.admin import site

from app.admin.problem import ProblemAdmin
from app.admin.user import UserAdmin
from app.models.problem import Problem, ProblemCategory, ProblemTag
from app.models.user import User

site.register(Problem, ProblemAdmin)
site.register(ProblemCategory)
site.register(ProblemTag)
site.register(User, UserAdmin)
