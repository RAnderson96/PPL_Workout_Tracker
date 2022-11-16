from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.record_repository as record_repository
import repositories.user_repository as user_repository



user_blueprint = Blueprint("user", __name__)


@user_blueprint.route("/user", methods=['GET'])

def show_user():
    user = user_repository.select_all()
    
    return render_template('/user/index.html', user=user)