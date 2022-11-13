from flask import Flask, render_template
from repositories import exercise_repository, user_repository, workout_repository
from flask import Flask, render_template, request, redirect
from models.exercise import Exercise
from models.user import User
from models.workout import Workout


app = Flask(__name__)

from controllers.workout_controller import books_blueprint

app.register_blueprint(books_blueprint)



@app.route('/')
def home():
    workouts = workout_repository.select_all()
    return render_template('index.html', workouts = workouts)



if __name__ == '__main__':
    app.run(debug=True)