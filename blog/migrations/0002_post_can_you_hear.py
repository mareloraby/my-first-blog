# Generated by Django 2.2.18 on 2021-02-08 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='can_You_Hear',
            field=models.BooleanField(default=True),
        ),
    ]
