from flask import request, render_template, redirect, url_for
from flask_jwt_extended import JWTManager,create_access_token,jwt_required,get_jwt_identity,get_jwt
from ..models.users_models import User


def landing():
    return render_template("Access.html")

# Register Client
def Register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        details = {"name": name, "email": email, "password": password}
        
        if (User.check_client_email(email)):
            print("found")
        else:
            print("not found")
      
        if (User.create_user(details)):
         

# Login Client

def Clientslogin():
    if request.method == "POST":
        name = request.form["username"]
        password = request.form["password"]

        LoginDetails = {"name": name, "password": password}
       
        if (User.login_user(LoginDetails)):
          

# Register Admin

def signup():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
 
        SignupDetails = {"name": name, "email": email, "password": password}
        
        # check if user exist using email
        
        if (User.check_admin_email(email)):
            print("found")
        else:
            print("not found")
        
      
        if (User.admin_signup(SignupDetails)):
         

# Login Admin

def login():
    if request.method == "POST":
        name = request.form["username"]
        password = request.form["password"]

        AdminDetails = {"name": name, "password": password}
        
        
        
if (User.admin_login(AdminDetails)):
         

