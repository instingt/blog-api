# Generated by Django 2.0.5 on 2018-05-20 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_at',
            field=models.DateTimeField(null=True, verbose_name='Опубликовано в'),
        ),
    ]
