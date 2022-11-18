
from os import name
from django.urls import path
from .views import CourseDetailPage, main
urlpatterns = [

    path('', main),
    path('detail/<int:pk>/', CourseDetailPage.as_view(), name='course-detail'),
]
