# Generated by Django 3.1.5 on 2021-01-15 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20210114_1931'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='photo_10',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_7',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_8',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_9',
        ),
        migrations.AlterField(
            model_name='listing',
            name='bathrooms',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
        migrations.AlterField(
            model_name='listing',
            name='lot_size',
            field=models.DecimalField(decimal_places=1, max_digits=5),
        ),
        migrations.AlterField(
            model_name='listing',
            name='state',
            field=models.CharField(max_length=100),
        ),
    ]
