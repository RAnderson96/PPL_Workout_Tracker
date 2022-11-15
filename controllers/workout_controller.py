from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.exercise import Exercise
import repositories.exercise_repository as exercise_repository
import repositories.workout_repository as workout_repository

workout_blueprint = Blueprint("workout", __name__)


# SHOW
# GET '/books/<id>'
@workout_blueprint.route("/workout/<index>", methods=['GET'])

def show_workout(index):
    push_a = exercise_repository.select_specific_workout('Push', 1, 'A')
    pull_a = exercise_repository.select_specific_workout('Pull', 2, 'A')
    legs = exercise_repository.select_specific_workout('Legs', 3, 'Normal')
    push_b = exercise_repository.select_specific_workout('Push', 4, 'B')
    pull_b = exercise_repository.select_specific_workout('Pull', 5, 'B')
    all_workouts = [push_a, pull_a, legs, push_b, pull_b]

    
    return render_template('workouts/index.html', workout=all_workouts[int(index)-1])



#     workout = workout_repository.select(workout_num)
#     return render_template('books/show.html', book = book)