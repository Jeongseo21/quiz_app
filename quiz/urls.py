from django.urls import path, include
from .views import helloAPI, randomQuiz

urlpatterns = [
    path("hello/", helloAPI),
    path("<int:id>/", randomQuiz),
]

#배포관련 설치해야하는 파일
# django-cors-headers : cors에러 방지
# gunicorn : 배포를 위한 도구
# psycopg2-binary : postgresql 사용을 위한 패키지
# whitenoise : 정적파일의 사용을 돕는 미들웨어
# dj-database-url : postgresql 사용을 위한 패키지
