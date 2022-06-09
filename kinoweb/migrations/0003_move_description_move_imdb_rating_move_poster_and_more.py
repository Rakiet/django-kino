# Generated by Django 4.0.5 on 2022-06-07 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kinoweb', '0002_move_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='move',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='move',
            name='imdb_rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='move',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='posters'),
        ),
        migrations.AddField(
            model_name='move',
            name='premiere',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='move',
            name='year',
            field=models.PositiveSmallIntegerField(default=2000),
        ),
    ]