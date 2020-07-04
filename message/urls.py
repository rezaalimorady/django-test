from django.urls import path, include
from . import views

app_name = 'message'
urlpatterns = [
    path('', views.inbox, name='inbox'),
]
