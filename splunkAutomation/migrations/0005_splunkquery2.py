# Generated by Django 2.0.5 on 2018-08-10 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('splunkAutomation', '0004_executecommands'),
    ]

    operations = [
        migrations.CreateModel(
            name='SplunkQuery2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query_text', models.CharField(max_length=1000)),
                ('query_resolution_commands', models.CharField(default='', max_length=300)),
                ('resolve_conf', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
