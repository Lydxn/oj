from django.db import models

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
    slug = models.SlugField(unique=True)
    statement = models.TextField(blank=True)
    category = models.ForeignKey(ProblemCategory, on_delete=models.CASCADE)
    tags = models.ManyToManyField(ProblemTag, blank=True)
    time_limit = models.FloatField()
    memory_limit = models.PositiveIntegerField()

    def __str__(self):
        return self.name
