# Generated by Django 2.2.6 on 2019-10-15 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat_module', '0001_initial'),
        ('project_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='chat',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='chat_module.Chat'),
        ),
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(0, '互联网'), (1, '金融'), (2, '电商'), (3, '教育'), (4, '游戏'), (5, '科学'), (6, '工业'), (7, '公益'), (8, '政府'), (9, '其他')], default=0),
        ),
    ]
