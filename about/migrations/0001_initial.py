# Generated by Django 2.1.7 on 2019-11-23 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Convenor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='img/convenors')),
                ('name', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('fb_id', models.URLField()),
                ('mail_id', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Coordinator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('fb_id', models.URLField()),
                ('mail_id', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HeadCoordinator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('fb_id', models.URLField()),
                ('mail_id', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('fb_id', models.URLField()),
                ('mail_id', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
    ]
