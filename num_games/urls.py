from django.urls import path, include
from  . import views

app_name = 'num_games'
urlpatterns = [
    # домашняя страница
    path('', views.index, name='index'),
    # старт для игры ИИ. страница выбора диапазона
    path('start_ai_play', views.start_ai_play, name='start_ai_play'),
    # старт для игры человека. страница выбора диапазона
    path('start_user_play', views.start_user_play, name='start_user_play'),
    # страница игры человека
    path('play_user/<int:game_id>/', views.play_user, name='play_user'),
    # страница игры ИИ
    path('play_ai/<int:game_id>/', views.play_ai, name='play_ai'),
    # страница результата игры
    path('game_result/<int:game_id>/result/', views.game_result, name='game_result'),
]


