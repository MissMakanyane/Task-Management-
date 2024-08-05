from flask import Flask,url_for,redirect,Response,request,render_template,session, jsonify
from flask import Flask, render_template, request, redirect, url_for
from models import admin

def admin_signup():
    user = {
    "full_name" : request.json.get('full_name'),
    "email" : request.json.get('email'),
    "cell_number" : request.json.get('cell_number'),
    "password" : request.json.get('password')
    }

    # Check if username already exists
    users.create_user(user)
    return jsonify({'message': 'succes'}), 400



