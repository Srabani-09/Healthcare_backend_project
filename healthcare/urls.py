from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('auth/register/', views.RegisterView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('patients/', views.PatientListCreateView.as_view(), name='patient-list-create'),
    path('patients/<int:pk>/', views.PatientDetailView.as_view(), name='patient-detail'),
    path('doctors/', views.DoctorListCreateView.as_view(), name='doctor-list-create'),
    path('doctors/<int:pk>/', views.DoctorDetailView.as_view(), name='doctor-detail'),
    path('mappings/', views.MappingListCreateView.as_view(), name='mapping-list-create'),
    path('mappings/<int:pk>/', views.MappingDeleteView.as_view(), name='mapping-delete'),
    path('mappings/patient/<int:patient_id>/', views.PatientDoctorMappingView.as_view(), name='patient-doctor-mappings'),
]

