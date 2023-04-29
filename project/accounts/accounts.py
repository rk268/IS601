import math
import datetime
from flask import Blueprint, flash, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from sql.db import DB
from accounts.forms import CreateAccountForm
from werkzeug.datastructures import MultiDict
accounts = Blueprint('accounts', __name__, url_prefix='/accounts',template_folder='templates')


@accounts.route("/create", methods=["GET","POST"])
@login_required
def create():
    user_id = current_user.get_id()
    form = CreateAccountForm()  
    return render_template("account_form.html", form=form, type="Create")

@accounts.route("/list", methods=["GET"])
@login_required
def list():
    user_id = current_user.get_id()
    form = CreateAccountForm()
    return render_template("account_form.html", form=form, type="Create")

    

@accounts.route("/deposit", methods=["GET","POST"])
@login_required
def deposit():
    user_id = current_user.get_id()
    form = CreateAccountForm()
    return render_template("account_form.html", form=form, type="Create")

@accounts.route("/withdraw", methods=["GET","POST"])
@login_required
def withdraw():
    user_id = current_user.get_id()
    form = CreateAccountForm()
    return render_template("account_form.html", form=form, type="Create")

@accounts.route("/transfer", methods=["GET","POST"])
@login_required
def transfer():
    user_id = current_user.get_id()
    form = CreateAccountForm()
    return render_template("account_form.html", form=form, type="Create")

@accounts.route("/profile", methods=["GET","POST"])
@login_required
def profile():
    user_id = current_user.get_id()
    form = CreateAccountForm()
    return render_template("account_form.html", form=form, type="Create")

    
    

