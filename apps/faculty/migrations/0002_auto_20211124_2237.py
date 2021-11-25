# Generated by Django 3.2.4 on 2021-11-24 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='leave_duration',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='faculty',
            name='on_leave',
            field=models.BooleanField(default=False),
        ),
    ]
