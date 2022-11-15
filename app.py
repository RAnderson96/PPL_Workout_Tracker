from flask import Flask, render_template
from repositories import exercise_repository, user_repository, workout_repository, pull_a_repository, pull_b_repository, push_a_repository, push_b_repository, legs_repository
from flask import Flask, render_template, request, redirect
from models.exercise import Exercise
from models.user import User
from models.workout import Workout


app = Flask(__name__)

# from controllers.workout_controller import books_blueprint

# app.register_blueprint(workout_blueprint)



@app.route('/')
def home():
    push_a = push_a_repository.select_all()
    pull_a = pull_a_repository.select_all()
    legs = legs_repository.select_all()
    push_b = push_b_repository.select_all()
    pull_b = pull_b_repository.select_all()
    all_workouts = [push_a, pull_a, legs, push_b, pull_b]

    return render_template('index.html', all_workouts = all_workouts)



if __name__ == '__main__':
    app.run(debug=True)