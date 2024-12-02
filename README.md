# 댄스 아카데미 관리 시스템

## 프로젝트 소개
Django와 React를 사용한 댄스 학원 관리 시스템입니다.

## 기술 스택
- Backend: Django 5.0.1, Django REST Framework 3.14.0
- Frontend: React 18, TypeScript, Vite
- Database: SQLite (개발), MySQL (운영)

## 설치 및 실행 방법
### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## 환경 설정
1. backend/.env.example을 backend/.env로 복사하고 필요한 값을 설정
2. frontend/.env.example을 frontend/.env로 복사하고 필요한 값을 설정

## 개발 가이드라인
- 커밋 메시지는 명확하고 구체적으로 작성
- 새로운 기능은 feature/ 브랜치에서 개발
- PR 전 테스트 코드 작성 필수
- 코드 리뷰 후 main 브랜치에 머지