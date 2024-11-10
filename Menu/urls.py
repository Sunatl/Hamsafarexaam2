from django.urls import path
from .views import *

urlpatterns = [
    path("",base,name="base"),
    path("HOME",home,name="home"),
    path('logout/',user_logout, name='logout'),


    # user
    path("User",UserListView.as_view(),name="list_u"),
    path("detail_u/<int:pk>",UserDetailView.as_view(),name="detail_u"),
    path("update_u/<int:pk>",UserUpdateView.as_view(),name="update_u"),
    path("create_u",UserCreateView.as_view(),name="create_u"),
    path("delete_u/<int:pk>",UserDeleteView.as_view(),name="delete_u"),
    
    
    # Aplication
    path("Talant",TalantListView.as_view(),name="list_m"),
    path("detail_m/<int:pk>",TalantDetailView.as_view(),name="detail_m"),
    path("update_m/<int:pk>",TalantUpdateView.as_view(),name="update_m"),
    path("create_m",TalantCreateView.as_view(),name="create_m"),
    path("delete_m/<int:pk>",TalantDeleteView.as_view(),name="delete_m"),
    
    path("Aplication",AplicationListView.as_view(),name="list_o"),
    path("detail_o/<int:pk>",AplicationDetailView.as_view(),name="detail_o"),
    path("update_o/<int:pk>",AplicationUpdateView.as_view(),name="update_o"),
    path("create_o",AplicationCreateView.as_view(),name="create_o"),
    path("delete_o/<int:pk>",AplicationDeleteView.as_view(),name="delete_o"),
]