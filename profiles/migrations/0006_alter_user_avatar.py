# Generated by Django 4.1.7 on 2023-03-04 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_alter_user_avatar_alter_user_friends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='img', verbose_name='avatar'),
        ),
    ]
