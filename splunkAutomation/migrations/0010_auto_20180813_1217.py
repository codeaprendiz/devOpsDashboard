# Generated by Django 2.0.5 on 2018-08-13 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('splunkAutomation', '0009_auto_20180813_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='executecommand',
            name='issue',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='splunkquery',
            name='query_text',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
