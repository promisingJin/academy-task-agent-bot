from django.core.management.base import BaseCommand
from apps.teachers.models import Teacher


class Command(BaseCommand):
    help = '테스트 교사 데이터를 생성합니다.'

    def handle(self, *args, **options):
        # 기존 테스트 데이터가 있다면 삭제
        Teacher.objects.filter(teacher_id__in=['teacher001', 'teacher002']).delete()
        
        # 테스트 데이터 생성
        test_teachers = [
            {
                'teacher_id': 'teacher001',
                'passwd': '12345678',
                'teacher_name': 'May',
                'age': 33,
                'position': '강사',
                'sex': 'female'
            },
            {
                'teacher_id': 'teacher002',
                'passwd': '98765',
                'teacher_name': '이미영',
                'age': 30,
                'position': '강사',
                'sex': 'female'
            }
        ]
        
        created_teachers = []
        for teacher_data in test_teachers:
            teacher, created = Teacher.objects.get_or_create(
                teacher_id=teacher_data['teacher_id'],
                defaults=teacher_data
            )
            if created:
                created_teachers.append(teacher)
                self.stdout.write(
                    self.style.SUCCESS(
                        f'교사가 생성되었습니다: {teacher.teacher_name} (ID: {teacher.id}, Login ID: {teacher.teacher_id})'
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f'교사가 이미 존재합니다: {teacher.teacher_name} (ID: {teacher.id}, Login ID: {teacher.teacher_id})'
                    )
                )
        
        total_count = Teacher.objects.count()
        self.stdout.write(
            self.style.SUCCESS(
                f'\n총 {len(created_teachers)}명의 교사가 생성되었습니다. '
                f'전체 교사 수: {total_count}명'
            )
        ) 