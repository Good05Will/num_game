# Generated by Django 5.0.7 on 2024-07-28 12:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_num', models.IntegerField(default=1)),
                ('end_num', models.IntegerField(default=100)),
                ('num_rounds', models.IntegerField(default=1)),
                ('is_finished', models.BooleanField(default=False)),
                ('guess_num', models.IntegerField(blank=True, null=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GameAI',
            fields=[
                ('game_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='num_games.game')),
            ],
            options={
                'verbose_name_plural': 'AI games',
            },
            bases=('num_games.game',),
        ),
        migrations.CreateModel(
            name='GameUser',
            fields=[
                ('game_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='num_games.game')),
                ('secret_num', models.IntegerField(default=0)),
                ('answer', models.TextField(default='unknowne')),
            ],
            options={
                'verbose_name_plural': 'USER games',
            },
            bases=('num_games.game',),
        ),
    ]
