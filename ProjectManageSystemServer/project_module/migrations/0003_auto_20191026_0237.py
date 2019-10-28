# Generated by Django 2.2.6 on 2019-10-25 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_module', '0002_auto_20191016_0245'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': '项目', 'verbose_name_plural': '项目'},
        ),
        migrations.RemoveField(
            model_name='project',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='project',
            name='start_time',
        ),
        migrations.AddField(
            model_name='project',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='结束日期'),
        ),
        migrations.AddField(
            model_name='project',
            name='start_date',
            field=models.DateField(blank=True, null=True, verbose_name='开始日期'),
        ),
        migrations.AlterField(
            model_name='project',
            name='chat',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='chat_module.Chat', verbose_name='聊天室'),
        ),
        migrations.AlterField(
            model_name='project',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(blank=True, max_length=256, verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='project',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='删除标志'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=16, verbose_name='项目名'),
        ),
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, '互联网'), (2, '金融'), (3, '电商'), (4, '教育'), (5, '游戏'), (6, '科学'), (7, '工业'), (8, '公益'), (9, '政府'), (10, '其他')], default=0, verbose_name='项目类型'),
        ),
    ]