# Generated by Django 4.2.7 on 2023-12-21 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0011_drink_category_drink'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food_Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('title_en', models.CharField(blank=True, max_length=100, null=True)),
                ('title_uz', models.CharField(blank=True, max_length=100, null=True)),
                ('title_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, max_length=100, null=True)),
                ('description_en', models.TextField(blank=True, max_length=100, null=True)),
                ('description_uz', models.TextField(blank=True, max_length=100, null=True)),
                ('description_ru', models.TextField(blank=True, max_length=100, null=True)),
                ('price', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Eat_Menu',
        ),
        migrations.AddField(
            model_name='comic',
            name='images',
            field=models.ImageField(help_text='Image', null=True, unique=True, upload_to='files/covers'),
        ),
        migrations.AddField(
            model_name='drink',
            name='description_en',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='drink',
            name='description_ru',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='drink',
            name='description_uz',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='drink',
            name='title_en',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='drink',
            name='title_ru',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='drink',
            name='title_uz',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]