# Generated by Django 3.1.4 on 2020-12-08 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_postagem'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Postagem',
        ),
    ]
