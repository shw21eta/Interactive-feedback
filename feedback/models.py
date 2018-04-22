from django.db import models

# Create your models here.
class Teacher(models.Model):
    name=models.CharField(max_length=20)
    courseCode=models.CharField(max_length=20)
    course=models.CharField(max_length=40)
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Student(models.Model):
    prn=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.prn

class Feedback(models.Model):
    prn=models.CharField(max_length=20)
    courseCode=models.CharField(max_length=20)
    q1=models.IntegerField()
    q2=models.IntegerField()
    q3=models.IntegerField()
    q4=models.IntegerField()
    q5=models.IntegerField()
    q6=models.IntegerField()

    def __str__(self):
        return self.courseCode


class Message(models.Model):
    f_id= models.ForeignKey('Feedback',on_delete=models.CASCADE)
    msg = models.CharField(max_length=40)
    status = models.IntegerField()                      #status shows strangth--1   , weakness---0
    timestamp= models.DateTimeField(
        auto_now_add=True,
        auto_now=False
    )

    def __str__(self):
        return self.msg


class Questions(models.Model):
    question= models.CharField(max_length=100)

    def __str__(self):
        return self.question
