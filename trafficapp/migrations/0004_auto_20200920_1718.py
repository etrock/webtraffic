# Generated by Django 2.1.15 on 2020-09-20 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trafficapp', '0003_delete_trafficrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trafficgeneraterequest',
            name='url',
            field=models.CharField(max_length=255),
        ),
    ]