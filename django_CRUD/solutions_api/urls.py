from django.urls import path, include
from rest_framework.routers import DefaultRouter
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
]
