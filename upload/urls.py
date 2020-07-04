from django.urls import path
from . import views

app_name = 'upload'
urlpatterns = [
    path('', views.index_upload, name='index_upload'),
    path('new/', views.UploadView, name='UploadView'),
]
