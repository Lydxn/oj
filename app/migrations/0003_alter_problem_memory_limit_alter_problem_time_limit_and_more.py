# Generated by Django 4.0.6 on 2023-04-28 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_problem_difficulty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='memory_limit',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='problem',
            name='time_limit',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='submission',
            name='memory',
            field=models.PositiveBigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='time',
            field=models.PositiveBigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='submissioncase',
            name='memory',
            field=models.PositiveBigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='submissioncase',
            name='num',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='submissioncase',
            name='time',
            field=models.PositiveBigIntegerField(null=True),
        ),
    ]
