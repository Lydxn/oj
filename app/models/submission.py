from django.db import models
from django.utils import timezone

from algogym import settings
from app.judge import JudgeClient
from app.models.language import Language
from app.models.problem import Problem
from app.models.user import User


class Status(models.TextChoices):
    J = 'J', 'Judging'
    Q = 'Q', 'In Queue'
    AC = 'AC', 'Accepted'
    WA = 'WA', 'Wrong Answer'
    MLE = 'MLE', 'Memory Limit Exceeded'
    TLE = 'TLE', 'Time Limit Exceeded'
    NZE = 'NZE', 'Non Zero Exit'
    RE = 'RE', 'Runtime Error'
    CE = 'CE', 'Compile Error'
    IE = 'IE', 'Internal Error'


class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    source = models.TextField(max_length=65536)
    status = models.CharField(max_length=3, choices=Status.choices, default='Q')
    time = models.PositiveBigIntegerField(null=True)
    memory = models.PositiveBigIntegerField(null=True)
    error = models.TextField(blank=True)
    submitted = models.DateTimeField(default=timezone.now)

    def __init__(self, *args, **kwargs):
        super(Submission, self).__init__(*args, **kwargs)

        self.HANDLERS = {
            'case-begin': self._handle_case_begin,
            'case-end': self._handle_case_end,
            'case-verdict': self._handle_case_verdict,
            'compile-error': self._handle_compile_error,
            'internal-error': self._handle_internal_error,
            'judging-begin': self._handle_judging_begin,
            'judging-end': self._handle_judging_end
        }

        self.status_priority = ('J', 'Q', 'AC', 'WA', 'MLE', 'TLE', 'NZE', 'RE', 'CE', 'IE').index

    def judge(self):
        with JudgeClient(settings.JUDGE_ADDRESS) as client:
            for data in client.submit(self):
                try:
                    header = data['header']
                    self.HANDLERS[header](data)
                except KeyError:
                    raise Exception(f'Judge gave an unknown header: {data}')

    @property
    def finished(self):
        return self.status not in ('J', 'Q')

    def _handle_case_begin(self, data):
        pass

    def _handle_case_end(self, data):
        status = 'J'
        time = 0
        memory = 0

        for case in SubmissionCase.objects.filter(submission=self):
            status = max(status, case.status, key=self.status_priority)
            if case.time:
                time += case.time
            if case.memory:
                memory += case.memory

        self.status = status

        if status != 'TLE':
            self.time = time
        if status != 'MLE':
            self.memory = memory

    def _handle_case_verdict(self, data):
        case = SubmissionCase(
            submission=self,
            num=data['case-num'],
            input=data['input'],
            output=data['output'],
            status=Status(data['status']),
            time=data['cpu-time'],
            memory=data['memory'],
            message=data['message']
        )
        case.save()

    def _handle_compile_error(self, data):
        self.status = 'CE'
        self.error = data['error']

    def _handle_internal_error(self, data):
        self.status = 'IE'
        self.error = data['error']

    def _handle_judging_begin(self, data):
        self.status = 'J'

    def _handle_judging_end(self, data):
        self.save()

        self.problem.update()

    def __str__(self):
        return f'Submission {self.id} by {self.user} on {self.problem}'


class SubmissionCase(models.Model):
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    num = models.PositiveIntegerField()
    input = models.CharField(max_length=50)
    output = models.CharField(max_length=50)
    status = models.CharField(max_length=3, choices=Status.choices)
    time = models.PositiveBigIntegerField(null=True)
    memory = models.PositiveBigIntegerField(null=True)
    message = models.CharField(max_length=50)

    @property
    def time_fmt(self):
        if self.time:
            return f'{self.time/1e9:.3f}s'
        else:
            return '#.###s'

    def __str__(self):
        return f'Case #{self.num}: {self.status} ({self.time_fmt}, {self.memory}kB)'
