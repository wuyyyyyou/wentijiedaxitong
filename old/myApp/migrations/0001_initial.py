# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-23 06:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=150)),
                ('zannum', models.IntegerField(default=0)),
                ('cainum', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=150)),
                ('zannum', models.IntegerField(default=0)),
                ('cainum', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='problem',
            name='belong',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.Student'),
        ),
        migrations.AddField(
            model_name='answer',
            name='belong',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.Problem'),
        ),
        migrations.AddField(
            model_name='answer',
            name='belongs',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.Student'),
        ),
    ]