# Generated by Django 3.1 on 2020-10-22 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestCaseApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='api_key',
            field=models.CharField(blank=True, default='None', max_length=256, null=True, verbose_name='apikey'),
        ),
        migrations.AlterField(
            model_name='case',
            name='headers',
            field=models.CharField(max_length=1024, verbose_name='headers请求头'),
        ),
        migrations.AlterField(
            model_name='case',
            name='msg',
            field=models.CharField(max_length=256, verbose_name='测试用例额外描述'),
        ),
        migrations.AlterField(
            model_name='case',
            name='pre_fields',
            field=models.CharField(max_length=256, verbose_name='前置的字段'),
        ),
        migrations.AlterField(
            model_name='case',
            name='request_data',
            field=models.CharField(max_length=1024, verbose_name='请求参数'),
        ),
        migrations.AlterField(
            model_name='case',
            name='response',
            field=models.TextField(blank=True, default='None', null=True, verbose_name='实际结果'),
        ),
        migrations.AlterField(
            model_name='case',
            name='url',
            field=models.CharField(max_length=256, verbose_name='接口名称'),
        ),
    ]
