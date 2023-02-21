# Generated by Django 3.2 on 2023-02-21 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_remove_genretitle_unique_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(related_name='title_genre', through='reviews.GenreTitle', to='reviews.Genre'),
        ),
    ]
