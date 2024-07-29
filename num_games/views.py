from django.shortcuts import render, redirect
from .models import GameAI, GameUser, Game
from django.contrib.auth.decorators import login_required
import random



def index(request):
    return render(request, 'num_games/index.html')



@login_required()
def start_ai_play(request):
    '''Подготовка к игре, где угадывает ИИ. Выбор диапазона'''
    if request.method == 'POST':
        player = request.user
        max = int(request.POST['max'])
        game = GameAI.objects.create(player=player, end_num=max)
        return redirect('num_games:play_ai', game_id=game.id)
    else:
        return render(request, 'start_ai_play.html')


@login_required()
def start_user_play(request):
    '''Подготовка к игре, где угадывает ИИ. Выбор диапазона'''
    if request.method == 'POST':
        player = request.user
        max = int(request.POST['max'])
        game = GameUser.objects.create(player=player, end_num=max)
        game.create_secret_num()
        return redirect('num_games:play_user', game_id=game.id)
    else:
        return render(request, 'start_user_play.html')


@login_required()
def play_ai(request, game_id):
    '''Играет ИИ'''
    game = GameAI.objects.get(pk=game_id)
    if request.method == 'POST':
        feedback = request.POST['feedback']
        if feedback == 'угадал':
            game.finish_game(game.guess_num)
            return redirect('num_games:game_result', game_id=game.id)
        else:
            game.update_range(feedback)
            game.make_guess()
            return redirect('num_games:play_ai', game_id=game.id)
    else:
        if not game.is_finished:
            game.make_guess()
        return render(request, 'play_ai.html', {'game': game})







@login_required()
def play_user(request, game_id):
    '''Играет игрок'''
    game = GameUser.objects.get(pk=game_id)
    if request.method == 'POST':
        game.guess_num = int(request.POST['guess_num'])
        if game.guess_num == game.secret_num:
            game.finish_game(game.guess_num)
            return redirect('num_games:game_result', game_id=game.id)
        else:
            game.answer_ai()
            return redirect('num_games:play_user', game_id=game.id)
    else:
        if not game.is_finished:
            return render(request, 'play_user.html', {'game': game})



@login_required()
def game_result(request, game_id):
    '''Определяет итог игры'''
    game = Game.objects.get(pk=game_id)
    return render(request, 'game_result.html', {'game': game})