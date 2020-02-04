# Create your models here.
from django.utils import timezone
from django.db import models
import json


class ScrapyItem(models.Model):
    unique_id = models.CharField(max_length=100, null=True)
    data = models.TextField
    date = models.DateTimeField(default=timezone.now)

    @property
    def to_dict(self):
        data = {
            'data': json.loads(self.data),
            'date': self.date
        }
        return data

    def __str__(self):
        return self.unique_id