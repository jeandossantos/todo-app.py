# Generated by Django 4.2.2 on 2023-06-30 22:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=65)),
                ('email', models.CharField(max_length=65)),
                ('password', models.CharField(max_length=255, unique=True)),
            ],
        ),
    ]
