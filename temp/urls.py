from django.urls import path
from .views import user_profile, success_page, ForAdminPage, UserDetailView

urlpatterns = [
    path('', user_profile, name='home'),
    path('clay/', ForAdminPage.as_view(), name='users-list'),
    path('main/user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('success_page/', success_page, name='success_page'),
]
