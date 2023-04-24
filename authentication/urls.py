from django.urls import path, include
from .views import LoginView, LogoutView, SignupView, RoleGroupListCreateView, RoleGroupRetrieveUpdateDestroyView




urlpatterns = [
    # Auth views
    path('auth/login/',
         LoginView.as_view(), name='auth_login'),

    path('auth/logout/',
         LogoutView.as_view(), name='auth_logout'),

    path('auth/signup/',
         SignupView.as_view(), name='auth_signup'),

    path('auth/reset/',
         include('django_rest_passwordreset.urls',
                 namespace='password_reset')),

     path('groups/', RoleGroupListCreateView.as_view(), name='group-list'),
     path('groups/<int:pk>/', RoleGroupRetrieveUpdateDestroyView.as_view(), name='group-detail'),
    
]
