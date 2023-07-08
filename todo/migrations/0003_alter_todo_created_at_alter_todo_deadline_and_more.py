# Generated by Django 4.2.2 on 2023-07-08 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Criado'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='deadline',
            field=models.DateTimeField(null=True, verbose_name='Prazo'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.TextField(blank=True, verbose_name='Descrição'),
        ),
    ]
