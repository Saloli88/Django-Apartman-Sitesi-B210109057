# Generated by Django 4.1.4 on 2022-12-16 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='keywords',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
