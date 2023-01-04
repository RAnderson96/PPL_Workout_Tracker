from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.exercise import Exercise
from models.record import Record
from models.counter import Counter
import repositories.counter_repository as counter_repository
import repositories.exercise_repository as exercise_repository
import repositories.record_repository as record_repository

import pdb

record_blueprint = Blueprint("history", __name__)


@record_blueprint.route("/history", methods=['GET'])

def show_history():
    
    all_records = record_repository.select_exercise_reps()
    record_to_display = []
    record_of_sets = []
    for record in all_records:
        print(record)
        record_to_display.append(record[0])
    for set in record_to_display:
        print("this is the set loop")
        print(set)

    print(record_to_display)
        

    # all_exercises = []
    exercise_list = []
    for row in all_records:
        exercise_id_from_record = row[-1]
        exercise_list.append(list(exercise_repository.select(exercise_id_from_record)))
    # pdb.set_trace()
    list_of_names = []
    for row in exercise_list:
        # for object in row:
        list_of_names.append(row[0].exercise_name)
    # pdb.set_trace() 

    



        
    
    return render_template('/history/index.html', record_to_display=record_to_display, list_of_names=list_of_names)

#workout = all_workouts[int(index)-1], workout_sets = workout_sets, index=index

# DELETE ALL
# DELETE ALL '/history/delete'
@record_blueprint.route("/history/delete", methods=['POST'])
def delete_all_records():
    record_repository.delete_all()
    return redirect('/history')