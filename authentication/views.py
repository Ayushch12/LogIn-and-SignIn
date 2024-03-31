from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "authentication/index.html")


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        # Create a new user instance with keyword arguments
        myuser = User.objects.create(
            username=username,
            email=email,
            password=password  # Note: You shouldn't save passwords directly like this, consider using Django's built-in password hashing utilities.
        )
        # Update additional fields
        myuser.first_name = firstname
        myuser.last_name = lastname

        # Save the user object
        myuser.save()

        messages.success(request, "Your Account has been successfully created.")
        return redirect("signin")

    return render(request, "authentication/signup.html")




    return render(request, "authentication/signup.html")

def signin(request):
    return render(request, "authentication/signin.html")

def signout(request):
    pass




