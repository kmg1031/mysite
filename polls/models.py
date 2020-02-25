from django.db import models

# Create your models here.

class Furits(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=50)
    descript = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()
    cdate = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return [self.id, self.name, self.descript]

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = medels.DateTimeField('date published')


class Choice(models.Model):
    quetion = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
