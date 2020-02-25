from django.urls import path

from demo.documents import views

urlpatterns = [
    path('', views.DocumentView.as_view(), name='index'),
]
