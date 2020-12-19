from django.urls import path
from user import views

app_name = 'user'
urlpatterns = [
    path('',views.register, name='register'),
    path('user_login/',views.user_login,name='user_login'),
]