from __future__ import unicode_literals

from django.db import models

# The following lines were added

import datetime
from django.utils import timezone


class Standard(models.Model):
    standard_values = (
        ('Ninth', 'IX'),
        ('Tenth', 'X'),
        ('Eleventh', 'XI'),
        ('Twelfth', 'XII')
    )
    standard = models.CharField(max_length=20, choices=standard_values, default='')

    def __str__(self):
        return self.standard


class Question(models.Model):
    standard = models.ForeignKey(Standard)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published Recently?'


class Choice(models.Model):
    questions = models.ForeignKey(Question)
    choice_test = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_test
