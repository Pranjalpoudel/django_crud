from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import (
    PatientViewSet, UserDataViewSet, ImageUploadViewSet, 
    ProjectRegistrationViewSet, NoteViewSet, AppointmentAPIView, LoginView, ResultsView
)

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'userdata', UserDataViewSet)
router.register(r'images', ImageUploadViewSet)
router.register(r'projects', ProjectRegistrationViewSet)
router.register(r'notes', NoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('results/', ResultsView.as_view(), name='results'),
    path('appointment/', AppointmentAPIView.as_view(), name='appointment'),
    path('login/', LoginView.as_view(), name='login'),
    path('security-demo/', views.security_demo_view, name='security_demo'),
    path('sql-injection/', views.sql_injection_view, name='sql_injection'),
    path('csrf-demo/', views.csrf_demo_view, name='csrf_demo'),
    path('source-view/', views.source_view, name='source_view'),
]
