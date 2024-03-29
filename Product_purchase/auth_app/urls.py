from django.urls import path
from .views import user_signup,user_login,user_logout,change_password

urlpatterns = [
    path('signup/',user_signup, name='signup_url'),
    path('login/',user_login, name='login_url'),
    path('logout/',user_logout, name='logout_url'),
    path('change/',change_password, name='change_url')
]