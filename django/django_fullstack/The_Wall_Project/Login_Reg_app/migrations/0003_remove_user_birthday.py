# Generated by Django 2.2 on 2020-10-09 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login_Reg_app', '0002_comment_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='birthday',
        ),
    ]
