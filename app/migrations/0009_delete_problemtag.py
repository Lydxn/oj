# Generated by Django 4.2 on 2023-04-30 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_problemcategory_code'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProblemTag',
        ),
    ]
