# Generated by Django 3.2.6 on 2021-09-14 18:20

import blog.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, validators=[blog.models.sharp_valid], verbose_name='Tag_name')),
                ('descript', models.TextField(verbose_name='Description of tag name.')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('text', models.TextField(verbose_name='Text of post.')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date of create post.')),
                ('edited', models.DateTimeField(auto_now_add=True, verbose_name='Date of edit post.')),
                ('views', models.BigIntegerField(default=0, verbose_name='Count of view.')),
                ('is_moderated', models.BooleanField(default=False, verbose_name='If moderated.')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('tegs', models.ManyToManyField(related_name='posts', to='blog.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Text of comment.')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date of create comment.')),
                ('edited', models.DateTimeField(auto_now_add=True, verbose_name='Date of edit comment.')),
                ('is_moderated', models.BooleanField(default=False, verbose_name='If moderated.')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentes', to='blog.post')),
            ],
        ),
    ]
