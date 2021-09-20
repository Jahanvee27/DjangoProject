from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Question(models.Model):
    Question_text=models.CharField(max_length=200)
    answer=models.CharField(max_length=200,default='No answer suggested')
    pub_date=models.DateTimeField('date Published')
    def __str__(self):
        return self.Question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    choice_text=models.CharField(max_length=200)
    #votes=models.CharField(max_length=200)
    Question=models.ForeignKey(Question,on_delete=models.CASCADE)
    def __str__(self):
        return self.choice_text



