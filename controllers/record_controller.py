from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.exercise import Exercise
from models.record import Record
import repositories.exercise_repository as exercise_repository
import repositories.record_repository as record_repository
import pdb

record_blueprint = Blueprint("history", __name__)


@record_blueprint.route("/history", methods=['GET'])

def show_history():
    
 

    
    return render_template('/history/index.html')

#workout = all_workouts[int(index)-1], workout_sets = workout_sets, index=index