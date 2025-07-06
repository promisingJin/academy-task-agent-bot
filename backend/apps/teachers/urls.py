from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('', views.index, name = 'index'),
    path('admin/teachers/', views.AdminTeacherListView.as_view(), name='admin-teachers'),
]