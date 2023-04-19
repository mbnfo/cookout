# Generated by Django 4.0.1 on 2023-04-03 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooker', '0003_remove_food_ingredients_food_ingredients'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='ingredients',
        ),
        migrations.AddField(
            model_name='food',
            name='ingredients',
            field=models.ManyToManyField(to='cooker.Ingredient'),
        ),
    ]