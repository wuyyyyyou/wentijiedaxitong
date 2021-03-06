# Generated by Django 2.1.2 on 2018-12-02 03:00

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
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField(verbose_name='回答内容')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='回答时间')),
                ('good_num', models.IntegerField(default=0)),
                ('bad_num', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True, verbose_name='版块名称')),
                ('number', models.IntegerField(unique=True, verbose_name='板块序号')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='profile_pictures')),
            ],
            options={
                'db_table': 'profile',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_title', models.CharField(max_length=40, unique=True, verbose_name='问题标题')),
                ('question_text', models.TextField(verbose_name='详细描述')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='发布日期')),
                ('good_num', models.IntegerField(default=0, verbose_name='赞数')),
                ('bad_num', models.IntegerField(default=0, verbose_name='踩数')),
                ('grade', models.IntegerField(default=0, verbose_name='综合质量')),
                ('question_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question_and_answer.Category', verbose_name='板块名称')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to=settings.AUTH_USER_MODEL, verbose_name='提问者')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='联系方式')),
                ('univ', models.CharField(default='上海交通大学', max_length=20, verbose_name='学校')),
                ('major', models.CharField(default='---', max_length=20, verbose_name='专业')),
                ('profile', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='question_and_answer.Profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('univ', models.CharField(default='上海交通大学', max_length=20, verbose_name='学校')),
                ('major', models.CharField(default='---', max_length=20, verbose_name='研究方向')),
                ('profile', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='question_and_answer.Profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='question_and_answer.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to=settings.AUTH_USER_MODEL, verbose_name='回答者'),
        ),
    ]
