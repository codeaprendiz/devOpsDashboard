# Generated by Django 2.0.5 on 2018-08-13 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('splunkAutomation', '0008_auto_20180810_0950'),
    ]

    operations = [
        migrations.AddField(
            model_name='splunkquery',
            name='application',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='splunkquery',
            name='assembly',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='splunkquery',
            name='component',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='splunkquery',
            name='environment',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='splunkquery',
            name='organization',
            field=models.CharField(default='ukgrsps', max_length=10),
        ),
        migrations.AddField(
            model_name='splunkquery',
            name='platform',
            field=models.CharField(default='', max_length=30),
        ),
    ]
