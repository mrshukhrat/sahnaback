# Generated by Django 4.2.7 on 2023-12-20 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0006_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='address_en',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='address_ru',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='address_uz',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='banner',
            name='type_en',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='banner',
            name='type_ru',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='banner',
            name='type_uz',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
