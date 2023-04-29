from django.db import models
from django.utils import timezone

from app.models.user import User


class ProblemCategory(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProblemTag(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Problem(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=30, unique=True)
    statement = models.TextField(blank=True)
    category = models.ForeignKey(ProblemCategory, on_delete=models.CASCADE)
    difficulty = models.PositiveIntegerField()
    time_limit = models.PositiveIntegerField()
    memory_limit = models.PositiveIntegerField()
    num_attempts = models.PositiveIntegerField(default=0)
    num_solves = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def update(self):
        submissions = self.submission_set.filter(problem=self)
        ac_submissions = submissions.filter(status='AC')

        self.num_attempts = submissions.values('user').distinct().count()
        self.num_solves = ac_submissions.values('user').distinct().count()
        self.save()

    @property
    def user_solved(self):
        return

    def __str__(self):
        return self.name
