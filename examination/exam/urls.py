# exams/urls.py
from django.urls import path
from . import views 

urlpatterns = [
    #path('', views.home, name='index'),  # Home page
  #  path('login/', views.login, name='login'),  # Login page
  #  path('signup/', views.signup, name='signup'),  # Signup page
    #path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard page

]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    from django.urls import path
from . import views

urlpatterns = [
    path('exam/', views.exam_list, name='exam_list'),  # URL for listing exams
    path('exam/<int:exam_id>/', views.exam_start, name='exam_start'),  # URL for starting an exam
    path('exam_result/<int:exam_id>/', views.exam_result, name='exam_result'),
    path('exam/submit/<int:exam_id>/', views.submit_exam, name='submit_exam'),
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard page

]
