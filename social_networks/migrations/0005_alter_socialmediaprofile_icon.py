# Generated by Django 5.1 on 2024-08-27 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_networks', '0004_alter_socialmediaprofile_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmediaprofile',
            name='icon',
            field=models.CharField(choices=[('fa-facebook', 'Facebook'), ('fa-x', 'X'), ('fa-instagram', 'Instagram'), ('fa-linkedin', 'LinkedIn'), ('fa-youtube', 'YouTube'), ('fa-github', 'GitHub')], max_length=50),
        ),
    ]
