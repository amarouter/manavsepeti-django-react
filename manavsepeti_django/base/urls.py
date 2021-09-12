from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes, name="routes"),
    path('api/v1/users/profile', views.get_user_profile, name="user_profile"),
    path('api/v1/users', views.get_users, name="users"),
    path('api/v1/users/register', views.register_user, name="register"),
    path('api/v1/token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
