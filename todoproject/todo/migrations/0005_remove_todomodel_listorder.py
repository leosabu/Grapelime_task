# Generated by Django 4.0.3 on 2022-04-09 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_todomodel_listorder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todomodel',
            name='listorder',
        ),
    ]
