# Generated by Django 5.1 on 2024-08-14 12:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('img', models.ImageField(blank=True, null=True, upload_to='base_images/')),
                ('base_link', models.URLField(db_index=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('link', models.URLField(db_index=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('base_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rss.baselinks')),
            ],
        ),
    ]
