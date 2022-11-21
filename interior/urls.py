
from os import name
from django.urls import path
from .views import CourseDetailPage, main, CategoryListPage

urlpatterns = [
    path('', main),
    path('detail/<int:pk>/', CourseDetailPage.as_view(), name='course-detail'),
    # path('categories/', CategoryListPage.as_view(), name='categs'),
    # path('about/', about, name='about'),
]
