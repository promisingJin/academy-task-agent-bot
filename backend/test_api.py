import requests
import json

def test_get_teachers_api():
    """GET /api/admin/teachers API를 테스트합니다."""
    
    # API 엔드포인트 URL
    url = "http://localhost:8000/api/admin/teachers/"
    
    try:
        # GET 요청 보내기
        response = requests.get(url)
        
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")
        
        if response.status_code == 200:
            data = response.json()
            print("\n=== API 응답 데이터 ===")
            print(json.dumps(data, indent=2, ensure_ascii=False))
            
            # 데이터 검증
            print(f"\n=== 데이터 검증 ===")
            print(f"총 교사 수: {data.get('total_counts', 0)}")
            print(f"실제 교사 배열 길이: {len(data.get('teachers', []))}")
            
            # 각 교사 정보 출력
            for i, teacher in enumerate(data.get('teachers', []), 1):
                print(f"\n교사 {i}:")
                print(f"  - DB ID: {teacher.get('id')}")
                print(f"  - 로그인 ID: {teacher.get('teacher_id')}")
                print(f"  - 이름: {teacher.get('teacher_name')}")
                print(f"  - 나이: {teacher.get('age')}")
                print(f"  - 직책: {teacher.get('position')}")
                print(f"  - 성별: {teacher.get('sex')}")
                
        else:
            print(f"Error: {response.status_code}")
            print(f"Response: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("연결 오류: Django 서버가 실행 중인지 확인하세요.")
    except Exception as e:
        print(f"오류 발생: {e}")

def test_post_teachers_api():
    """POST /api/admin/teachers API를 테스트합니다."""
    
    # API 엔드포인트 URL
    url = "http://localhost:8000/api/admin/teachers/"
    
    # 테스트 데이터
    test_data = {
        "teacher_id": "teacher003",
        "passwd": "12345678",
        "teacher_name": "김철수",
        "age": 28,
        "position": "강사",
        "sex": "male"
    }
    
    try:
        # POST 요청 보내기
        response = requests.post(url, json=test_data)
        
        print(f"\n=== POST 요청 테스트 ===")
        print(f"Status Code: {response.status_code}")
        print(f"Request Data: {json.dumps(test_data, indent=2, ensure_ascii=False)}")
        
        if response.status_code == 201:
            data = response.json()
            print(f"\n=== 성공 응답 ===")
            print(json.dumps(data, indent=2, ensure_ascii=False))
            
        elif response.status_code == 400:
            data = response.json()
            print(f"\n=== 400 오류 응답 ===")
            print(json.dumps(data, indent=2, ensure_ascii=False))
            
        else:
            print(f"Error: {response.status_code}")
            print(f"Response: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("연결 오류: Django 서버가 실행 중인지 확인하세요.")
    except Exception as e:
        print(f"오류 발생: {e}")

def test_patch_teachers_api():
    """PATCH /api/admin/teachers API를 테스트합니다."""
    
    # API 엔드포인트 URL
    url = "http://localhost:8000/api/admin/teachers/"
    
    # 수정할 테스트 데이터
    patch_data = {
        "teacher_id": "teacher001",
        "passwd": "12345678",
        "teacher_name": "May",
        "age": 33,
        "position": "강사",
        "sex": "female"
    }
    
    try:
        # PATCH 요청 보내기
        response = requests.patch(url, json=patch_data)
        
        print(f"\n=== PATCH 요청 테스트 ===")
        print(f"Status Code: {response.status_code}")
        print(f"Request Data: {json.dumps(patch_data, indent=2, ensure_ascii=False)}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"\n=== 성공 응답 ===")
            print(json.dumps(data, indent=2, ensure_ascii=False))
            
        elif response.status_code == 400:
            data = response.json()
            print(f"\n=== 400 오류 응답 ===")
            print(json.dumps(data, indent=2, ensure_ascii=False))
            
        elif response.status_code == 404:
            data = response.json()
            print(f"\n=== 404 오류 응답 ===")
            print(json.dumps(data, indent=2, ensure_ascii=False))
            
        else:
            print(f"Error: {response.status_code}")
            print(f"Response: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("연결 오류: Django 서버가 실행 중인지 확인하세요.")
    except Exception as e:
        print(f"오류 발생: {e}")

def test_patch_nonexistent_teacher():
    """존재하지 않는 교사 ID로 PATCH 요청을 테스트합니다."""
    
    # API 엔드포인트 URL
    url = "http://localhost:8000/api/admin/teachers/"
    
    # 존재하지 않는 teacher_id
    patch_data = {
        "teacher_id": 999,
        "passwd": "12345678",
        "teacher_name": "존재하지않는교사",
        "age": 25,
        "position": "강사",
        "sex": "female"
    }
    
    try:
        # PATCH 요청 보내기
        response = requests.patch(url, json=patch_data)
        
        print(f"\n=== 존재하지 않는 교사 PATCH 테스트 ===")
        print(f"Status Code: {response.status_code}")
        print(f"Request Data: {json.dumps(patch_data, indent=2, ensure_ascii=False)}")
        
        if response.status_code == 404:
            data = response.json()
            print(f"\n=== 404 오류 응답 ===")
            print(json.dumps(data, indent=2, ensure_ascii=False))
            
        else:
            print(f"Error: {response.status_code}")
            print(f"Response: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("연결 오류: Django 서버가 실행 중인지 확인하세요.")
    except Exception as e:
        print(f"오류 발생: {e}")

def test_post_duplicate_teacher():
    """중복된 teacher_id로 POST 요청을 테스트합니다."""
    
    # API 엔드포인트 URL
    url = "http://localhost:8000/api/admin/teachers/"
    
    # 중복 테스트 데이터 (이미 존재하는 teacher_id)
    duplicate_data = {
        "teacher_id": "teacher001",
        "passwd": "12345678",
        "teacher_name": "중복테스트",
        "age": 25,
        "position": "강사",
        "sex": "female"
    }
    
    try:
        # POST 요청 보내기
        response = requests.post(url, json=duplicate_data)
        
        print(f"\n=== 중복 ID 테스트 ===")
        print(f"Status Code: {response.status_code}")
        print(f"Request Data: {json.dumps(duplicate_data, indent=2, ensure_ascii=False)}")
        
        if response.status_code == 400:
            data = response.json()
            print(f"\n=== 400 오류 응답 (중복 ID) ===")
            print(json.dumps(data, indent=2, ensure_ascii=False))
            
        else:
            print(f"Error: {response.status_code}")
            print(f"Response: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("연결 오류: Django 서버가 실행 중인지 확인하세요.")
    except Exception as e:
        print(f"오류 발생: {e}")

def test_delete_teacher_api():
    """DELETE /api/admin/teachers API를 테스트합니다."""
    url = "http://localhost:8000/api/admin/teachers/"
    delete_data = {
        "teacher_id": "teacher003"
    }
    try:
        response = requests.delete(url, json=delete_data)
        print(f"\n=== DELETE 요청 테스트 ===")
        print(f"Status Code: {response.status_code}")
        print(f"Request Data: {json.dumps(delete_data, indent=2, ensure_ascii=False)}")
        if response.status_code == 200:
            data = response.json()
            print(f"\n=== 성공 응답 ===")
            print(json.dumps(data, indent=2, ensure_ascii=False))
        elif response.status_code == 400:
            data = response.json()
            print(f"\n=== 400 오류 응답 ===")
            print(json.dumps(data, indent=2, ensure_ascii=False))
        elif response.status_code == 404:
            data = response.json()
            print(f"\n=== 404 오류 응답 ===")
            print(json.dumps(data, indent=2, ensure_ascii=False))
        else:
            print(f"Error: {response.status_code}")
            print(f"Response: {response.text}")
    except requests.exceptions.ConnectionError:
        print("연결 오류: Django 서버가 실행 중인지 확인하세요.")
    except Exception as e:
        print(f"오류 발생: {e}")

def test_delete_nonexistent_teacher():
    """존재하지 않는 teacher_id로 DELETE 요청을 테스트합니다."""
    url = "http://localhost:8000/api/admin/teachers/"
    delete_data = {
        "teacher_id": 999
    }
    try:
        response = requests.delete(url, json=delete_data)
        print(f"\n=== 존재하지 않는 교사 DELETE 테스트 ===")
        print(f"Status Code: {response.status_code}")
        print(f"Request Data: {json.dumps(delete_data, indent=2, ensure_ascii=False)}")
        if response.status_code == 404:
            data = response.json()
            print(f"\n=== 404 오류 응답 ===")
            print(json.dumps(data, indent=2, ensure_ascii=False))
        else:
            print(f"Error: {response.status_code}")
            print(f"Response: {response.text}")
    except requests.exceptions.ConnectionError:
        print("연결 오류: Django 서버가 실행 중인지 확인하세요.")
    except Exception as e:
        print(f"오류 발생: {e}")

if __name__ == "__main__":
    print("=== 교사 API 테스트 ===")
    
    # GET 테스트
    test_get_teachers_api()
    
    # POST 테스트 (새로운 교사 생성)
    test_post_teachers_api()
    
    # PATCH 테스트 (교사 정보 수정)
    test_patch_teachers_api()
    
    # PATCH 테스트 (존재하지 않는 교사)
    test_patch_nonexistent_teacher()
    
    # POST 테스트 (중복 ID)
    test_post_duplicate_teacher()
    
    # DELETE 테스트 (교사 삭제)
    test_delete_teacher_api()
    
    # DELETE 테스트 (존재하지 않는 교사 삭제)
    test_delete_nonexistent_teacher() 