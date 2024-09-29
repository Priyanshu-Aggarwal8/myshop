from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Feedback
from .forms import FeedbackForm
from django.contrib import messages
from django.http import JsonResponse
import firebase_admin
from firebase_admin import auth
import pyrebase

config = {
  apiKey: "AIzaSyA4XX3dGZv22X3tvGqvnKKJPdGNiqUkIL0",
  authDomain: "myshop-f2954.firebaseapp.com",
  projectId: "myshop-f2954",
  storageBucket: "myshop-f2954.appspot.com",
  messagingSenderId: "454542907350",
  appId: "1:454542907350:web:bc96f45b0e34a1c1cb3677",
  measurementId: "G-J6CJ4C6Y5D"
}
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()

def home(request):
	day = database.child('Data').child('Day').get().val()
	id = database.child('Data').child('Id').get().val()
	projectname = database.child('Data').child('Projectname').get().val()
	return render(request,"Home.html",{"day":day,"id":id,"projectname":projectname })

def create_user(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = auth.create_user(email=email, password=password)
    return JsonResponse({'uid': user.uid})

def get_user(request, uid):
    user = auth.get_user(uid)
    return JsonResponse({'email': user.email})

def index(request):
    user = "priyanshu"
    products_num = 7
    product = Product.objects.all().order_by('id')[:4]
    suits = Product.objects.filter(brand__title= "best")
    return render(request, "products/home.html",{
        "name": user,
        "product_num": products_num,
        "products": product,
    })

def signup(request):
    return render(request, "products/signup.html")

def login(request):
    return render(request, "products/login.html")

def trending(request):
    return render(request, "products/trending.html")

def cart(request):
    return render(request, "products/cart.html")

def cat_product(request, product):
    if product in ["shirts","shoes","dresses","suits"]:
        return HttpResponse(f"Here is the list of {product}")
    else:
        return HttpResponse("The page you are looking for doesn't exist") 
    
def product_page(request, product_brand, product_slug):
    product = Product.objects.get(slug = product_slug)
    form = FeedbackForm()
    reviews = Feedback.objects.filter(product = product)
    if request.method == "GET":
        return render(request, "products/productpage.html", {
            "product": product,
            "form": form,
            "reviews" : reviews,
        })
    else:
        form = FeedbackForm(request.POST)
        if(form.is_valid()):
            feedback = Feedback(
                name = form.cleaned_data["name"],
                email = form.cleaned_data["email"],
                description = form.cleaned_data["description"],
                product = product
            )
            feedback.save()
            messages.success(request, "Your feedback was submitted successfully")
        
        return render(request, "products/productpage.html", {
            "product": product,
            "form": form,
            "reviews" : reviews,
        })
