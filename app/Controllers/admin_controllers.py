from flask import Flask,url_for,redirect,Response,request,render_template,flash, jsonify
from ..models.admin_models import Data_admin
from flask_jwt_extended import JWTManager,create_access_token,jwt_required,get_jwt_identity,get_jwt

def admin_signup():
 if request.method == 'POST':
    full_name = request.json.get('full_name')
    email = request.json.get('email')
    cell_number = request.json.get('cell_number')
    password = request.json.get('password')
   
    signup_data = {'full_name': full_name,  'email': email,'cell_number': cell_number, 'password': password,}
    Data_admin.create_new(signup_data)
   
    return jsonify({'message': 'succesful'})

def admin_login():
    if request.method == "POST":
        name = request.form["username"]
        password = request.form["password"]

        LoginDetails = {"name": name, "password": password}
        if Data_admin.create_new(LoginDetails):
           return jsonify({'message': 'succesful'})
            
    return True   