from flask import Flask,url_for,redirect,Response,request,render_template,flash, jsonify
from ..models.admin_models import Data_admin
from flask_jwt_extended import JWTManager,create_access_token,jwt_required,get_jwt_identity,get_jwt


def Register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        details = {"name": name, "email": email, "password": password}
       
    
        if (User.create_user(details)):