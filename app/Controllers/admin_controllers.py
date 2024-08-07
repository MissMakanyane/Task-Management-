from flask import Flask,url_for,redirect,Response,request,render_template,flash, jsonify
from ..models.admin_models import Get_admin
from flask_jwt_extended import JWTManager,create_access_token,jwt_required,get_jwt_identity,get_jwt

def admin_signup():
 if request.method == 'POST':
    full_name = request.json.get('full_name')
    email = request.json.get('email')
    cell_number = request.json.get('cell_number')
    password = request.json.get('password')
    
    signup = {'full_name': full_name,  'email': email,'cell_number': cell_number, 'password': password,}
    Get_admin.create_new(signup)
   
    return jsonify({'message': 'succesful'})

