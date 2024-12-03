# Generated by Django 5.1.1 on 2024-11-12 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0014_alter_ve_ma_qr_ve'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
    ]
