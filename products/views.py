from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product, Feedback
from .forms import FeedbackForm
from django.contrib import messages
#-----------------------------------------------------------------------------------------------------------
# Import necessary modules and models
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *

# Define a view function for the home page
def home(request):
    return render(request, "products/home.html")

# Define a view function for the login page
def login_page(request):
    # Check if the HTTP request method is POST (form submission) 
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
            return redirect("login")
        
        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)
        
        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return redirect("login")
        else:
            # Log in the user and redirect to the home page upon successful login
            login(request)
            return redirect("home")
    
    # Render the login page template (GET request)
    return render(request, "products/login.html")

# Define a view function for the registration page
def register_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if a user with the provided username already exists
        user = User.objects.filter(username=username)
        
        if user.exists():
            # Display an information message if the username is taken
            messages.info(request, "Username already taken!")
            return redirect("signup")
        
        # Create a new User object with the provided information
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        
        # Set the user's password and save the user object
        user.set_password(password)
        user.save()
        
        # Display an information message indicating successful account creation
        messages.info(request, "Account created Successfully!")
        return redirect("products/signup.html")
    
    # Render the registration page template (GET request)
    return render(request, "products/signup.html")

#--------------------------------------------------------------------------------------------------------
def index(request):
    user = "Priyanshu"
    products_num = 7
    product = Product.objects.all().order_by('id')[:4]
    suits = Product.objects.filter(brand__title= "best")
    return render(request, "products/home.html",{
        "user": user,
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

#---------------------------------------------------------------------------------------------------------

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

#---------------------------------------------------------------------------------------------------------

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {'products': products})

def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'products/cart.html', {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request, product_id):
    product = Product.objects.get(slug=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('view_cart')

def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('view_cart')