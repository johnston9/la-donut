# Generated by Django 3.2.4 on 2021-07-06 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_comment_user_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='recipe',
        ),
    ]
