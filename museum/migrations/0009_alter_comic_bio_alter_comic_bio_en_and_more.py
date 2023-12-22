# Generated by Django 4.2.7 on 2023-12-21 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0008_comic_banner_comic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comic',
            name='bio',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='comic',
            name='bio_en',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='comic',
            name='bio_ru',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='comic',
            name='bio_uz',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='comic',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='comic',
            name='last_name_en',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='comic',
            name='last_name_ru',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='comic',
            name='last_name_uz',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
