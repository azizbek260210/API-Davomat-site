# Generated by Django 5.0.4 on 2024-04-19 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff_attendance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='staff',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
    ]
