# Generated by Django 4.2.2 on 2023-07-08 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_todo_created_at_alter_todo_deadline_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Prazo'),
        ),
    ]