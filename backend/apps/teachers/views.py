from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Teacher
from .serializers import TeacherSerializer, TeacherDetailSerializer

# Create your views here.

def index(request) :
    return HttpResponse("hello teacher apps")

class AdminTeacherListView(APIView):
    """
    관리자가 교사 목록을 조회, 생성, 수정, 삭제하는 API
    GET /api/admin/teachers - 교사 목록 조회
    POST /api/admin/teachers - 새로운 교사 생성
    PATCH /api/admin/teachers - 교사 정보 수정
    DELETE /api/admin/teachers - 교사 삭제
    """
    
    def get(self, request):
        try:
            # 모든 교사 조회
            teachers = Teacher.objects.all()
            
            # 시리얼라이저를 통해 데이터 변환
            serializer = TeacherSerializer(teachers, many=True)
            
            # 응답 데이터 구성
            response_data = {
                "total_counts": teachers.count(),
                "teachers": serializer.data
            }
            
            return Response(response_data, status=status.HTTP_200_OK)
            
        except Exception as e:
            # 서버 내부 오류
            return Response(
                {"error": "서버 내부 오류가 발생했습니다."}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def post(self, request):
        try:
            # 요청 데이터 검증
            serializer = TeacherDetailSerializer(data=request.data)
            
            if not serializer.is_valid():
                return Response(
                    {
                        "error": "잘못된 요청입니다.",
                        "details": serializer.errors
                    }, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # teacher_id가 이미 존재하는지 확인
            teacher_id = serializer.validated_data.get('teacher_id')
            if Teacher.objects.filter(teacher_id=teacher_id).exists():
                return Response(
                    {
                        "error": "이미 존재하는 교사 ID입니다.",
                        "teacher_id": teacher_id
                    }, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # 새로운 교사 생성
            teacher = serializer.save()
            
            # 생성된 교사 정보 반환
            response_serializer = TeacherSerializer(teacher)
            
            return Response(
                {
                    "message": "교사가 성공적으로 생성되었습니다.",
                    "teacher": response_serializer.data
                }, 
                status=status.HTTP_201_CREATED
            )
            
        except Exception as e:
            # 서버 내부 오류
            return Response(
                {"error": "서버 내부 오류가 발생했습니다."}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def patch(self, request):
        try:
            # teacher_id가 요청에 포함되어 있는지 확인
            teacher_id = request.data.get('teacher_id')
            if not teacher_id:
                return Response(
                    {
                        "error": "teacher_id가 필요합니다.",
                        "details": "수정할 교사의 ID를 제공해주세요."
                    }, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # 해당 teacher_id를 가진 교사가 존재하는지 확인
            try:
                teacher = Teacher.objects.get(teacher_id=teacher_id)
            except Teacher.DoesNotExist:
                return Response(
                    {
                        "error": "교사를 찾을 수 없습니다.",
                        "teacher_id": teacher_id
                    }, 
                    status=status.HTTP_404_NOT_FOUND
                )
            
            # 요청 데이터 검증 (부분 업데이트)
            serializer = TeacherDetailSerializer(teacher, data=request.data, partial=True)
            
            if not serializer.is_valid():
                return Response(
                    {
                        "error": "잘못된 요청입니다.",
                        "details": serializer.errors
                    }, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # 교사 정보 수정
            updated_teacher = serializer.save()
            
            # 수정된 교사 정보 반환
            response_serializer = TeacherSerializer(updated_teacher)
            
            return Response(
                {
                    "message": "교사 정보가 성공적으로 수정되었습니다.",
                    "teacher": response_serializer.data
                }, 
                status=status.HTTP_200_OK
            )
            
        except Exception as e:
            # 서버 내부 오류
            return Response(
                {"error": "서버 내부 오류가 발생했습니다."}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def delete(self, request):
        try:
            teacher_id = request.data.get('teacher_id')
            if not teacher_id:
                return Response(
                    {"error": "teacher_id가 필요합니다.", "details": "삭제할 교사의 ID를 제공해주세요."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            try:
                teacher = Teacher.objects.get(teacher_id=teacher_id)
            except Teacher.DoesNotExist:
                return Response(
                    {"error": "교사를 찾을 수 없습니다.", "teacher_id": teacher_id},
                    status=status.HTTP_404_NOT_FOUND
                )
            teacher.delete()
            return Response(
                {"message": "교사가 성공적으로 삭제되었습니다.", "teacher_id": teacher_id},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"error": "서버 내부 오류가 발생했습니다."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )