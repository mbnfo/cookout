from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Ingredient(models.Model):
    name = models.CharField( max_length= 50)
    Info = models.CharField(max_length= 1250, default =  'skip')
    Suggested_Url = models.CharField(max_length=100, default =  'skip')
    Picture = models.ImageField(upload_to='media/Ingredients', default='media/IMG-20220304-WA0002-1.jpg')

    def __str__(self):
        return self.name

class Utensil(models.Model):
    Name = models.CharField( max_length= 50)
    Info = models.CharField(max_length= 1250, default =  'skip')
    Suggested_Url = models.CharField(max_length=100, default =  'skip')
    Picture = models.ImageField(upload_to='media/Utensils', default='media/IMG-20220304-WA0002-1.jpg')

    def __str__(self):
        return self.Name

class Food(models.Model):
    Name = models.CharField(max_length= 50)
    Description = models.CharField(max_length= 350)
    Chef = models.CharField(max_length= 50)
    Tutorial = models.CharField(max_length = 1250)
    Tutorial_Link = models.CharField(max_length= 100)
    Cooking_Time = models.IntegerField(default= 5)
    Rating = models.IntegerField(default = 10)
    Image = models.ImageField(upload_to='media/', default='media/IMG-20220304-WA0002-1.jpg')
    ingredients = models.ManyToManyField(Ingredient)
    utensils = models.ManyToManyField(Utensil)

    def __str__(self):
        return self.Name


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    no_ings = models.IntegerField(default = 1)
    ingredients = models.ManyToManyField(Ingredient)
    available = models.ManyToManyField(Food)

    def __str__(self):
        return self.user.username 