# Generated by Django 4.0.1 on 2023-04-06 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooker', '0006_alter_profile_available_delete_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='Info',
            field=models.CharField(default='skip', max_length=1250),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='Suggested_Url',
            field=models.CharField(default='skip', max_length=100),
        ),
        migrations.AlterField(
            model_name='utensil',
            name='Info',
            field=models.CharField(default='skip', max_length=1250),
        ),
        migrations.AlterField(
            model_name='utensil',
            name='Suggested_Url',
            field=models.CharField(default='skip', max_length=100),
        ),
    ]
