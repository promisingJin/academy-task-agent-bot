from rest_framework import serializers
from .models import Student

#학생이 회원가입 할 필요가 있나요? - 추후 삭제
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'