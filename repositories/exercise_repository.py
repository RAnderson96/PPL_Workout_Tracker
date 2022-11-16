from db.run_sql import run_sql
import pdb
from models.exercise import Exercise


def save(exercise):
    sql = "INSERT INTO exercises (exercise_name, num_sets, num_reps, weights, workout_group, workout_num, workout_varient) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [exercise.exercise_name, exercise.num_sets, exercise.num_reps, exercise.weights, exercise.workout_group, exercise.workout_num, exercise.workout_varient]
    results = run_sql(sql, values)
    id = results[0]['id']
    exercise.id = id
    return  exercise



def select(id):
    workout = []
    sql = "SELECT * FROM exercises WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    for row in results:
        exercise = Exercise(row['exercise_name'], row['num_sets'], row['num_reps'], row['weights'], row['workout_group'], row['workout_num'], row['workout_varient'], row['id'])
        workout.append(exercise)
    return workout




def select_specific_workout(workout_group, workout_num, workout_varient):
    workout = []
    sql = "SELECT * FROM exercises WHERE workout_group = %s AND workout_num = %s AND workout_varient = %s"
    values = [workout_group, workout_num, workout_varient]
    results = run_sql(sql, values)
    for row in results:
        exercise = Exercise(row['exercise_name'], row['num_sets'], row['num_reps'], row['weights'], row['workout_group'], row['workout_num'], row['workout_varient'], row['id'])
        workout.append(exercise)
    return workout


def select_specific_workout_num(workout_group, workout_varient):
    
    sql = "SELECT MIN(workout_num) FROM exercises WHERE workout_group = %s AND workout_varient = %s"
    values = [workout_group, workout_varient]
    results = run_sql(sql, values)
    return results[0]['min']

   
def update(exercise):
    sql = "UPDATE exercises SET (exercise_name, num_sets, num_reps, weights, workout_group, workout_num, workout_varient) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [exercise.exercise_name, exercise.num_sets, exercise.num_reps, exercise.weights, exercise.workout_group, exercise.workout_num, exercise.workout_varient, exercise.id]
  
    # sql = "UPDATE exercises SET (exercise_name, num_sets, num_reps, weights, workout_group, workout_num, workout_varient) VALUES (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    # values = [exercise.exercise_name, exercise.num_sets, exercise.num_reps, exercise.weights, exercise.workout_group, exercise.workout_num, exercise.workout_varient, exercise.id]
    # values = [exercise.num_sets, exercise.num_reps, exercise.id]
    result = run_sql(sql, values) 
    

    

# def delete_all():
#     sql = "DELETE FROM exercises"
#     run_sql(sql)

def delete(id):
    sql = "DELETE FROM exercises WHERE id = %s"
    values = [id]
    run_sql(sql, values)
