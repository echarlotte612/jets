# Generated by Django 3.1.4 on 2020-12-01 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20201201_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='sighting',
            name='report',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cryptid',
            name='description',
            field=models.TextField(),
        ),
    ]
