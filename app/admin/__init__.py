from django.contrib.admin import site

from app.admin.problem import ProblemAdmin
from app.admin.user import UserAdmin
from app.models.language import Language
from app.models.problem import Problem, ProblemCategory, ProblemTag
from app.models.submission import Submission
from app.models.user import User


site.register(Language)
site.register(Problem, ProblemAdmin)
site.register(ProblemCategory)
site.register(ProblemTag)
site.register(Submission)
site.register(User, UserAdmin)
