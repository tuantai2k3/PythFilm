# Generated by Django 5.1.1 on 2024-11-08 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_combo_img_combo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='combo',
            name='img_combo',
            field=models.ImageField(null=True, upload_to='img_combo/'),
        ),
    ]
