# Generated by Django 5.1.1 on 2024-11-08 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_alter_phim_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='combo',
            name='img_combo',
            field=models.ImageField(blank=True, null=True, upload_to='img_combo/'),
        ),
    ]
