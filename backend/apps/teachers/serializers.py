from rest_framework import serializers
from .models import Teacher
from rest_framework_simplejwt.tokens import RefreshToken

class TeacherSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Teacher
        fields = ['id', 'teacher_id', 'teacher_name', 'age', 'position', 'sex']
        read_only_fields = ['id']

class TeacherDetailSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Teacher
        fields = '__all__'
        read_only_fields = ['id']

class TeacherLoginSerializer(serializers.Serializer) :
    '''
    로그인 요청의 필드중 role == "teacher" 일때 실행
    '''
    teacher_id = serializers.CharField()
    passwd = serializers.CharField()

    def validate(self, data) :
        #teacher 테이블에서 teacher_id 확인
        try :
            teacher = Teacher.objects.get(teacher_id = data['teacher_id'])
        except Teacher.DoesNotExist :
            raise serializers.ValidationError("존재하지 않는 교사입니다.")
        
        #teacher 테이블에서 passwd확인
        if teacher.passwd != data['passwd'] :
            raise serializers.ValidationError("비밀번호가 올바르지 않습니다.")
        
        refresh = RefreshToken.for_user(teacher)

        return {
            #상태, 메시지, 토큰 등에 대한 정보
            "status": "success",
            "message": "로그인 성공",
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
            #유저 - 선생 혹은 관리자 일 수 있다.
            "user" : {
                "id" : teacher.id,
                "teacher_id" : teacher.teacher_id,
                "age" : teacher.age,
                "teacher_name" : teacher.teacher_name,
                "position" : teacher.position,
                "sex" : teacher.sex
                }
        }
        
