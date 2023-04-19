from django.shortcuts import render, redirect, HttpResponse
from .models import Food, Ingredient, Utensil, Profile
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import random

def signin(request):
    usertag = random.randrange(0, 10000)
    username = "chef" + str(usertag)
    email_obj = str(usertag) + '@nomail.com'
    createuser = User.objects.create_user(username=username,  email=email_obj, password= username)
    createuser.save()
    user_login = auth.authenticate(username=username, password = username)
    auth.login(request, user_login)
        
    user_model = User.objects.get(username=username)
    new_profile = Profile.objects.create(user=user_model, id=user_model.id)
    new_profile.save()
    return redirect('/')

@login_required(login_url='signin')
def home(request):
    food = Food.objects.all()
    user = Profile.objects.get(user = request.user.id)
    for i in user.available.all():
        user.available.remove(i)

    for i in user.ingredients.all():
        user.ingredients.remove(i)

    return render (request, 'home.html', {
        'food':food
    })

def processing(request):
    if request.method == 'GET':
        text = request.GET["ingredients"]
    return redirect('/cook')

@login_required(login_url='signin')
def cook(request):
    user_obj = Profile.objects.get(user = request.user.id)
    ingredient = Ingredient.objects.all()

    if user_obj is not None: 
        for ingr in user_obj.ingredients.all():
            food = Food.objects.get(ingredients = ingr)
            user_obj.available.add(food)

    if request.method == 'POST':
        ing = request.POST["ingredient"]
        item = Ingredient.objects.get(name = ing)
        user_obj.ingredients.add(item)
        user_obj.no_ings += 1
        user_obj.save()
    

    return render(request, 'cook.html', {
        'user':user_obj,
        'ingredient':ingredient,
    })

def food(request, f):
    gg = Food.objects.get(Name = f)
    return render(request, 'food.html', {
        'gg':gg,
    })

@login_required(login_url='signin')
def post(request):
    ingredient = Ingredient.objects.all()
    utensil = Utensil.objects.all()
    if request.method == 'POST':
        ing = request.POST['ingredient']
        ute = request.POST['utensil']
        recip = request.POST['recipe']
        desc = request.POST['description']
        tut = request.POST['tutorial']
        tut_url = request.POST['tutorial_url']
        time = request.POST['time']
        img = request.POST['image']

        food = Food.objects.create(Name = recip, Description = desc, Tutorial = tut, Tutorial_Link = tut_url, time = time, image = img, ingredients = ing, utensis = ute) 
        return redirect('/')
    return render(request, 'post.html', {
        'ingredient':ingredient,
        'utensil':utensil,
    })