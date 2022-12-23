

from django.urls import path
from .views import coursedetail, detailcategory, main, payment, categories, about, success_pay, courses, connection
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', main),
    path('detail/<int:pk>/', coursedetail, name='course'),
    path('payment', payment, name='payment'),
    path('success_pay/', success_pay, name='success'),

    path('categories/', categories, name='categories'),
    path('courses/', courses, name='courses'),

    path('category/<int:pk>/', detailcategory, name='detcat'),
    path('connection', connection, name='conn'),
    path('about/', about, name='about'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)