from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('num_games:index')
        else:
            context = {'error':True}
            return render(request, 'users/login.html', context)
    else:
        return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'num_games/index.html')

def register(request):
    '''Регистрирует нового пользователя.'''
    if request.method != 'POST':
        # Выводит пустую форму регистрации
        form = UserCreationForm()
    else:
        # Обработка данных
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Выполнение входа и перенаправление на домашнюю страницу
            login(request, new_user)
            return redirect('num_games:index')
    # Вывести пустую и недействительную форму
    context = {'form' : form}
    return render(request, 'users/register.html', context)
