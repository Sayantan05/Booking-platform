# Generated by Django 3.1.5 on 2021-05-14 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_user_display_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image_url',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
    ]