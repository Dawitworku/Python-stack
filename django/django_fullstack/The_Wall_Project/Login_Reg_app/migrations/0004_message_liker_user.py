# Generated by Django 2.2 on 2020-10-11 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login_Reg_app', '0003_remove_user_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='liker_user',
            field=models.ManyToManyField(related_name='liked_messages', to='Login_Reg_app.User'),
        ),
    ]
