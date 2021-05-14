from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('sudoku-rules', views.sudoku, name="sudoku"),
    path('play-sudoku', views.play, name="play"),
    path('login', views.login_page, name="login"),
    path('logout', views.logout_user, name="logout"),
    path('upload-file', views.upload_file, name="upload"),
]