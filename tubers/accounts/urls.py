from django.urls import path

from  . import views

urlpatterns=[
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('logout', views.logout_user, name="logout"), #we cannot name views as logout bz its inbuld feature already defined in django
    path('dashboard', views.dashboard, name="dashboard"),
]
 