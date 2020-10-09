# Generated by Django 2.2 on 2020-10-07 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Lec_LR_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Koala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('talent', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='koalas', to='Lec_LR_app.User')),
                ('users_votes', models.ManyToManyField(related_name='voted_koalas', to='Lec_LR_app.User')),
            ],
        ),
    ]
