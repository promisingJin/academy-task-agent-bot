from django.db import models

# Create your models here.

class Teacher(models.Model) :
    # 자동 생성되는 primary key
    id = models.AutoField(primary_key=True)
    # 로그인용 아이디 (unique=True로 중복 방지)
    teacher_id = models.CharField(max_length=50, unique=True)
    passwd = models.CharField(max_length=100)
    age = models.IntegerField()
    teacher_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} - {self.teacher_name} ({self.teacher_id})"