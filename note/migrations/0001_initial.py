# Generated by Django 3.1.5 on 2021-03-10 09:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChecklistItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=90)),
                ('checked', models.BooleanField(default=False)),
                ('position', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=60)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('is_archieved', models.BooleanField(default=False)),
                ('created_by',
                 models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='note_created',
                                   to=settings.AUTH_USER_MODEL)),
                ('tagged_users',
                 models.ManyToManyField(blank=True, related_name='note_tagged', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated_at'],
                'abstract': False,
            },
        ),
    ]