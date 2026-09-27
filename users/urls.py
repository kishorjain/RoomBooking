from django.urls import path
from .views import UsersHomeView


urlpatterns = [
    #path('', views.users_home, name='users_home'),
    path('', UsersHomeView.as_view(), name='users_home'),

]
