import uuid

from django.db import models

# Create your models here.
from django.urls import reverse


class Emp(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    emp_name = models.CharField(max_length=100)
    man_id = models.ForeignKey('Emp', on_delete=models.SET_NULL, blank = True, null=True)

    def get_absolute_url(self):
        return reverse('employee-detail', args=[str(self.emp_id)])

    def __str__(self):
        return f'{self.emp_id}, ({self.emp_name})'


