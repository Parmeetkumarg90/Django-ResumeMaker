# Generated by Django 5.1.5 on 2025-01-22 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0009_alter_user_data_edu_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_data',
            name='intro_image',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='user-images/', verbose_name='User Image'),
        ),
    ]
