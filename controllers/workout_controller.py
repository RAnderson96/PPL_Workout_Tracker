from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.exercise import Exercise
import repositories.exercise_repository as exercise_repository
import repositories.workout_repository as workout_repository

workout_blueprint = Blueprint("workout", __name__)


# SHOW
# GET '/books/<id>'
# @workout_blueprint.route("/workout/<workout_num>", methods=['GET'])
# def show_workout(workout_num):
#     workout = workout_repository.select(workout_num)
#     return render_template('books/show.html', book = book)