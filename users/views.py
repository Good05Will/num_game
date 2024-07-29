from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm


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
