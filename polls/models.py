from django.db import models
from django.db.models.fields import DateTimeField

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200);
    pub_date = DateTimeField();
    def str(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE);
    choice_text = models.CharField(max_length=100);
    vote = models.IntegerField(default=0);
    def str(self):
        return self.choice_text