# Generated by Django 2.2.6 on 2019-11-24 00:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0017_auto_20191123_2318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='party',
            name='category',
        ),
        migrations.RemoveField(
            model_name='party',
            name='save_the_date_opened',
        ),
        migrations.RemoveField(
            model_name='party',
            name='save_the_date_sent',
        ),
        migrations.RemoveField(
            model_name='party',
            name='type',
        ),
    ]
