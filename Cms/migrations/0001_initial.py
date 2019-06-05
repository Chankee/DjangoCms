# Generated by Django 2.2.1 on 2019-06-05 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('description', models.CharField(max_length=200, verbose_name='描述')),
                ('leader', models.CharField(max_length=50, verbose_name='负责人')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键')),
                ('finish_time', models.DateTimeField(auto_now=True, verbose_name='完成产品时间')),
            ],
            options={
                'verbose_name': '产品信息',
                'db_table': 'Product',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('description', models.CharField(max_length=200, verbose_name='描述')),
                ('leader', models.CharField(max_length=50, verbose_name='负责人')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键')),
                ('finish_time', models.DateTimeField(auto_now=True, verbose_name='完成产品时间')),
                ('product_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_product', to='Cms.Product')),
            ],
            options={
                'verbose_name': '项目表',
                'db_table': 'Project',
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('description', models.CharField(max_length=200, verbose_name='描述')),
                ('leader', models.CharField(max_length=50, verbose_name='负责人')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键')),
                ('finish_time', models.DateTimeField(auto_now=True, verbose_name='完成模块时间')),
                ('project_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='module_project', to='Cms.Project')),
            ],
            options={
                'verbose_name': '模块表',
                'db_table': 'Module',
            },
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('description', models.CharField(max_length=200, verbose_name='描述')),
                ('leader', models.CharField(max_length=50, verbose_name='负责人')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键')),
                ('case_group', models.IntegerField(choices=[(1, 'UI用例'), (2, '接口用例'), (3, 'app用例')], verbose_name='用例所属组')),
                ('delete_time', models.DateTimeField(auto_now=True, verbose_name='用例删除时间')),
                ('module_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='case_module', to='Cms.Module')),
            ],
            options={
                'verbose_name': '公共字段表',
                'db_table': 'BaseTable',
                'abstract': False,
            },
        ),
    ]