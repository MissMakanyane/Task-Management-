from flask import Flask,url_for,redirect,Response,request,render_template,flash, jsonify
from ..models.admin_models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager,create_access_token,jwt_required,get_jwt_identity,get_jwt

def admin_signup():
    data = request.get_json()
    name = request.json.get('full_name')
    email = request.json.get('email')
    password = request.json.get('password')
  
    role = data.get('role', 'admin')
    if User.find_by_email(email):
        return jsonify({"msg": "User already exists"}), 409

    hashed_password = generate_password_hash(password, method="pbkdf2")
    new_user = User(email=email, name=name, password=hashed_password, role=role)
    new_user.save()

    return jsonify({"msg": "User registered successfully"}), 201

def admin_login():
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        user = User.find_by_email(email)
        if user and check_password_hash(user.password, password):
            access_token = create_access_token(identity={"email": user.email, "role": user.role})
            return jsonify({"access token": access_token ,"role": user.role, "password":user.password} ), 200

        return jsonify({"msg": "Invalid credentials"}), 401