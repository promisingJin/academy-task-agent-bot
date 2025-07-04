from django.db import models

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    class_id = models.IntegerField()
    name = models.CharField(max_length=30)
    birth_date = models.IntegerField()
    gender = models.CharField(max_length=10, choices=(('male', 'male'), ('female', 'female')))

class Teacher(models.Model) :
    teacher_id = models.IntegerField(primary_key=True)
    age = models.IntegerField
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)

