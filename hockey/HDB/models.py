from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Player(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    draft_year = models.DateField()
