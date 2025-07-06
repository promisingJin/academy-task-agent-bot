import os
import django
import sys

# Django 설정 로드
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AcademyTaskAgentBot.settings')
django.setup()

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

def generate_token():
    """JWT 토큰을 생성합니다."""
    
    # 기본 사용자 생성 (없다면)
    username = 'admin'
    email = 'admin@example.com'
    password = 'admin123'
    
    try:
        user = User.objects.get(username=username)
        print(f"기존 사용자 '{username}' 사용")
    except User.DoesNotExist:
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        print(f"새 사용자 '{username}' 생성됨")
    
    # JWT 토큰 생성
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)
    refresh_token = str(refresh)
    
    print("\n=== JWT 토큰 생성 완료 ===")
    print(f"사용자: {username}")
    print(f"Access Token: {access_token}")
    print(f"Refresh Token: {refresh_token}")
    
    print("\n=== API 사용 방법 ===")
    print("POST /api/admin/teachers 요청시 헤더에 추가:")
    print(f"Authorization: Bearer {access_token}")
    
    return access_token, refresh_token

if __name__ == "__main__":
    generate_token() 