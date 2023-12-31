# Generated by Django 4.2.6 on 2023-10-20 03:03

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragraph', models.CharField(max_length=250)),
                ('post_id', models.IntegerField()),
                ('likes', models.IntegerField()),
                ('dislikes', models.IntegerField()),
                ('date', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragraph', models.CharField(max_length=250)),
                ('num_likes', models.IntegerField()),
                ('num_dislikes', models.IntegerField()),
                ('date', models.TimeField()),
                ('num_comments', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Post_Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.IntegerField()),
                ('session_id', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(default=home.models.generate_session_id, max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('lastname', models.CharField(max_length=15)),
                ('username', models.CharField(max_length=10)),
            ],
        ),
    ]
