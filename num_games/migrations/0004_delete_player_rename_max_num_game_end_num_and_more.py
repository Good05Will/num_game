# Generated by Django 5.0.7 on 2024-07-30 16:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('num_games', '0003_player'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.DeleteModel(
            name='Player',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='max_num',
            new_name='end_num',
        ),
        migrations.RemoveField(
            model_name='game',
            name='name',
        ),
        migrations.AddField(
            model_name='game',
            name='player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
