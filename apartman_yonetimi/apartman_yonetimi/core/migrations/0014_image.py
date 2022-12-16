# Generated by Django 4.1.4 on 2022-12-16 13:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_content_menu_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('content_id', models.UUIDField(default=uuid.uuid4, null=True)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='content_images')),
            ],
        ),
    ]
