from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='index'), #빈 url 이 들어온다면
    path("some_url", views.some_url, name='index'),
]