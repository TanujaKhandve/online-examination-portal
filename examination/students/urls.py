# exams/urls.py
from django.urls import path # type: ignore
from . import views
from .views import results


urlpatterns = [
    path('', views.base, name='base'),  # Home page
    path('login/', views.login_view, name='login'),  # Login page
    path('login_view/', views.login_view, name='login_view'),  # Login page
    path('register/', views.register, name='register'),  # Signup page
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard page
    path('exam_result/<int:exam_id>/', views.results, name='exam_result'),
    #path('exam/results/<int:exam_id>/', views.results, name='exam_result'),  # Exam result page
    path('student_profile/', views.student_profile, name='student_profile'),

    path('logout/', views.logout, name='logout'),  # Logout page
    path('about/', views.about, name='about'),  # About page
    path('contact/', views.contact_us, name='contactus'),  # Contact page
    path('aboutus/', views.aboutus, name='aboutus'),  # About page
    path('contactus/', views.contact, name='contact'),  # Contact page
]

from django.conf import settings # type: ignore
from django.conf.urls.static import static # type: ignore

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)