from django.db import models
from django.contrib.auth.models import User
import random


class Game(models.Model):
    '''Базовая модель игры'''
    player = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date_add = models.DateTimeField(auto_now_add=True)
    num_rounds = models.IntegerField(default=1)
    start_num = models.IntegerField(default=1)
    max_num = models.IntegerField(default=100)
    is_finished = models.BooleanField(default=False)
    guess_num = models.IntegerField(null=True, blank=True)

    def __str__(self):
        '''Строковое представление модели (для админки)'''
        return f"№ {self.id}. { self.__class__.__name__ }. {self.player.username.title()}."


    def finish_game(self, guessed_number):
        '''Завершает игру'''
        self.is_finished = True
        self.guess_num = guessed_number
        self.save()


class GameAI(Game):
    '''Модель игры в которой угадывает ИИ'''
    class Meta:
        verbose_name_plural = 'AI games'


    def update_range(self, feedback):
        '''Обновляет диапазон поиска в зависимости от ответа пользователя'''
        if feedback == 'меньше':
            self.max_num = self.guess_num - 1
        elif feedback == 'больше':
            self.start_num = self.guess_num + 1
        self.num_rounds += 1
        self.save()

    def make_guess(self):
        '''Генерирует следующий ответ для ИИ'''
        self.guess_num = (self.start_num + self.max_num) // 2
        self.save()



class GameUser(Game):
    '''Модель игры в которой угадывает человек'''
    secret_num = models.IntegerField(default=0)
    answer = models.TextField(default='unknowne')


    class Meta:
        verbose_name_plural = 'USER games'

    def create_secret_num(self):
        '''Генерирует случайное число из выбранного диапазона'''
        self.secret_num = random.randint(self.start_num, self.max_num)
        self.save()

    def answer_ai(self):
        '''Определяет подсказку в зависимости от ответа пользователя'''
        if self.guess_num > self.secret_num:
            self.answer = 'МЕНЬШЕ'
        elif self.guess_num < self.secret_num:
            self.answer = 'БОЛЬШЕ'
        self.num_rounds += 1
        self.save()