# Generated by Django 3.0.3 on 2020-03-29 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='expires_date',
            field=models.DateTimeField(null=True, verbose_name='expires at'),
        ),
    ]