# Generated by Django 5.0.6 on 2024-06-11 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_createpost_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(default='profiles/default.jpg', upload_to='profiles/%y/%m/%d'),
        ),
    ]
