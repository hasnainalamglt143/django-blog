# Generated by Django 5.0.3 on 2024-06-15 14:28

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_userprofile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createpost',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
