from flask import Blueprint
from ..Controllers import admin_controllers

app = Blueprint('admin', __name__)


app.route('/admin_signup', methods=['POST'])(admin_controllers.admin_signup)

# app.route('/admin_login', method=['POST'])(admin_controllers.admin_login)