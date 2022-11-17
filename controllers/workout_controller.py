from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.exercise import Exercise
from models.record import Record
from models.counter import Counter
import repositories.exercise_repository as exercise_repository
import repositories.record_repository as record_repository
import repositories.counter_repository as counter_repository
import pdb

workout_blueprint = Blueprint("workout", __name__)






#
@workout_blueprint.route("/workouts/<index>", methods=['GET'])

def show_workout(index):
    push_a = exercise_repository.select_specific_workout('Push', 1, 'A')
    pull_a = exercise_repository.select_specific_workout('Pull', 2, 'A')
    legs = exercise_repository.select_specific_workout('Legs', 3, '')
    push_b = exercise_repository.select_specific_workout('Push', 4, 'B')
    pull_b = exercise_repository.select_specific_workout('Pull', 5, 'B')
    all_workouts = [push_a, pull_a, legs, push_b, pull_b]
    workout=all_workouts[int(index)-1]
    workout_sets = []
    for exercise in workout:
        workout_sets.append(exercise.num_sets)
    

    
    return render_template('/workouts/index.html', workout = all_workouts[int(index)-1], workout_sets = workout_sets, index=index)



#     workout = workout_repository.select(workout_num)
#     return render_template('books/show.html', book = book)


@workout_blueprint.route("/workouts/<index>/record",  methods=['POST'])
def record_workout(index):
    push_a = exercise_repository.select_specific_workout('Push', 1, 'A')
    pull_a = exercise_repository.select_specific_workout('Pull', 2, 'A')
    legs = exercise_repository.select_specific_workout('Legs', 3, '')
    push_b = exercise_repository.select_specific_workout('Push', 4, 'B')
    pull_b = exercise_repository.select_specific_workout('Pull', 5, 'B')
    all_workouts = [push_a, pull_a, legs, push_b, pull_b]
    workout=all_workouts[int(index)-1]
    
    counter = Counter()
    counter_repository.save(counter)
    counter.workout_group_num +=1
    counter_repository.update(counter)
    for exercise in workout:
        record = Record(exercise)
        record.workout_dict.clear()

        # counter.exercise_id = exercise.id
        counter_repository.save(counter)
        
        
        for set in range(exercise.num_sets):
            reps = request.form[f'reps_{exercise.id}_{set}']
            weights = request.form[f'weights_{exercise.id}_{set}']      
            record.workout_dict.append([int(reps), float(weights)])
            
    
        # pdb.set_trace()
        record_repository.save(record)
    
       

    return redirect('/')



@workout_blueprint.route("/workouts/<index>/edit", methods=['GET'])
def edit_workout(index):
    push_a = exercise_repository.select_specific_workout('Push', 1, 'A')
    pull_a = exercise_repository.select_specific_workout('Pull', 2, 'A')
    legs = exercise_repository.select_specific_workout('Legs', 3, '')
    push_b = exercise_repository.select_specific_workout('Push', 4, 'B')
    pull_b = exercise_repository.select_specific_workout('Pull', 5, 'B')
    all_workouts = [push_a, pull_a, legs, push_b, pull_b]
    workout=all_workouts[int(index)-1]

    return render_template('/workouts/edit.html', workout=workout, index=index)


@workout_blueprint.route("/workouts/<index>", methods=['POST'])
def update_workout(index):
    push_a = exercise_repository.select_specific_workout('Push', 1, 'A')
    pull_a = exercise_repository.select_specific_workout('Pull', 2, 'A')
    legs = exercise_repository.select_specific_workout('Legs', 3, '')
    push_b = exercise_repository.select_specific_workout('Push', 4, 'B')
    pull_b = exercise_repository.select_specific_workout('Pull', 5, 'B')
    all_workouts = [push_a, pull_a, legs, push_b, pull_b]
    workout=all_workouts[int(index)-1]
    for exercise in workout:
        num_sets = int(request.form[f'num_sets_{(exercise.id)}'])
        num_reps = int(request.form[f'num_reps_{(exercise.id)}'])
        exercise_update = Exercise(exercise.exercise_name, num_sets, num_reps, exercise.weights, exercise.workout_group, exercise.workout_num, exercise.workout_varient, exercise.id)

        exercise_repository.update(exercise_update)
        
    return redirect('/')



# NEW
@workout_blueprint.route("/workouts/<index>/exercise/new", methods =['GET'])
def new_exercise(index):
    # push_a = exercise_repository.select_specific_workout('Push', 1, 'A')
    # pull_a = exercise_repository.select_specific_workout('Pull', 2, 'A')
    # legs = exercise_repository.select_specific_workout('Legs', 3, '')
    # push_b = exercise_repository.select_specific_workout('Push', 4, 'B')
    # pull_b = exercise_repository.select_specific_workout('Pull', 5, 'B')
    # all_workouts = [push_a, pull_a, legs, push_b, pull_b]
    # workout=all_workouts[int(index)-1]
    # workout_group = exercise_repository.select_workout_by_group(index)
    # workout_varient = exercise_repository.select_workout_varient(workout_group)

    return render_template("/workouts/new.html", index=index)


# CREATE
@workout_blueprint.route("/workouts/<index>/exercise/", methods=["POST"])
def create_exercise(index):
    push_a = exercise_repository.select_specific_workout('Push', 1, 'A')
    pull_a = exercise_repository.select_specific_workout('Pull', 2, 'A')
    legs = exercise_repository.select_specific_workout('Legs', 3, '')
    push_b = exercise_repository.select_specific_workout('Push', 4, 'B')
    pull_b = exercise_repository.select_specific_workout('Pull', 5, 'B')
    all_workouts = [push_a, pull_a, legs, push_b, pull_b]
    workout=all_workouts[int(index)-1]

    workout_group = exercise_repository.select_workout_by_group(index)
    workout_varient = exercise_repository.select_workout_varient(workout_group)
    
    new_exercise_name = request.form["exercise_name"]
    new_num_sets = int(request.form["num_sets"])
    new_num_reps = int(request.form["num_reps"])
    new_weights = float(request.form["weights"])
    # new_workout_group = request.form["workout_group"]
    # new_workout_varient = request.form["workout_varient"]
    new_workout_num = int(float(index))
    new_exercise = Exercise(new_exercise_name, new_num_sets, new_num_reps, new_weights, workout_group, new_workout_num, workout_varient)
   
    exercise_repository.save(new_exercise)
    return redirect("/")