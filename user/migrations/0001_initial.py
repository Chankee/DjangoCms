# Generated by Django 2.2.1 on 2019-05-11 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=32, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=256, verbose_name='登陆密码')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='用户邮箱')),
            ],
            options={
                'verbose_name': '用户信息',
                'db_table': 'UserInfo',
            },
        ),
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('token', models.CharField(max_length=50, verbose_name='token')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.UserInfo')),
            ],
            options={
                'verbose_name': '用户登陆token',
                'db_table': 'UserToken',
            },
        ),
    ]
