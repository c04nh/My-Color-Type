from django.db import models

class Color(models.Model):
    name = models.CharField(max_length=50)
    count = models.IntegerField(default=0)
    personality1 = models.CharField(max_length=50,null=True)
    personality2 = models.CharField(max_length=50,null=True)
    personality3 = models.CharField(max_length=50,null=True)
    personality4 = models.CharField(max_length=50,null=True)
    personality5 = models.CharField(max_length=50,null=True)
    personality6 = models.CharField(max_length=50,null=True)
    personality7 = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=50)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Question(models.Model):
    number = models.IntegerField(unique=True)
    content = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.number} - {self.content}'

class Choice(models.Model):
    content = models.CharField(max_length=100)
    question = models.ForeignKey(to='main.Question', on_delete=models.CASCADE)
    type = models.ForeignKey(to='main.Type', on_delete=models.CASCADE)

    def __str__(self):
        return self.content