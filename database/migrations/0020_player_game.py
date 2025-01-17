# Generated by Django 5.1.3 on 2024-11-30 06:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0019_nguoidung_vouchers_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_taken', models.FloatField()),
                ('correct_guess', models.BooleanField(default=False)),
                ('attempts', models.IntegerField(default=0)),
                ('correct_guesses', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('phim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.phim')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.player')),
            ],
        ),
    ]
