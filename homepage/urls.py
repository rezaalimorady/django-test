from django.urls import path, include
from . import views
from django.contrib.auth.views import login, logout
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'homepage'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', login),
    path('logout/', logout, {'template_name': 'registration/logout.html'}),
    path('register/', views.RegisterUser, name='RegisterUser'),
    path('change-password/', views.ChangePassword, name='ChangePassword'),
    path('profile/', views.UserProfileView, name='UserProfileView'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)