from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Refund(models.Model):
    title = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10, default='')
    account = models.CharField(max_length=100)
    account_name = models.CharField(max_length=100, default='')
    account_number = models.CharField(max_length=100)
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/')
    status = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title+'  '+self.name+' '+self.surname

    def __str__(self):
        return self.title+'  '+self.name+' '+self.surname

    def get_absolute_url(self):
        return reverse("refund:detail", kwargs={ "id" :self.id})
