# Generated by Django 4.1.4 on 2022-12-16 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_comment_faq'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='id_user',
            new_name='user_id',
        ),
    ]
