
from os import name
from django.urls import path
from .views import CourseDetailPage, main, payment, categories, about

urlpatterns = [
    path('', main),
    path('detail/<int:pk>/', CourseDetailPage.as_view(), name='course-detail'),
    path('payment', payment, name='course-pay'),
    path('success_pay/', payment, name='success'),
    path('categories/', categories, name='categories'),
    path('about/', about, name='about'),
]
