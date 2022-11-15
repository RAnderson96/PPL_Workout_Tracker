from db.run_sql import run_sql
import pdb
from models.exercise import Exercise
from models.workout import Workout
from models.legs import Leg
from models.pull import Pull
from models.push import Push


def save(exercise):
    sql = "INSERT INTO exercises (exercise_name, num_sets, num_reps, weights, workout_group, workout_num, workout_varient) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [exercise.exercise_name, exercise.num_sets, exercise.num_reps, exercise.weights, exercise.workout_group, exercise.workout_num, exercise.workout_varient]
    results = run_sql(sql, values)
    id = results[0]['id']
    exercise.id = id
    return  exercise



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
    
   

    



def save_pushes_a(exercise):
    sql = "INSERT INTO pushes_a (exercise_name, num_sets, num_reps, weights, workout_num) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [exercise.exercise_name, exercise.num_sets, exercise.num_reps, exercise.weights, exercise.workout_num]
    results = run_sql(sql, values)
    id = results[0]['id']
    exercise.id = id
    return  exercise

def save_pushes_b(exercise):
    sql = "INSERT INTO pushes_b (exercise_name, num_sets, num_reps, weights, workout_num) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [exercise.exercise_name, exercise.num_sets, exercise.num_reps, exercise.weights, exercise.workout_num]
    results = run_sql(sql, values)
    id = results[0]['id']
    exercise.id = id
    return  exercise


def save_pulls_a(exercise):
    sql = "INSERT INTO pulls_a (exercise_name, num_sets, num_reps, weights, workout_num) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [exercise.exercise_name, exercise.num_sets, exercise.num_reps, exercise.weights, exercise.workout_num]
    results = run_sql(sql, values)
    id = results[0]['id']
    exercise.id = id
    return  exercise

def save_pulls_b(exercise):
    sql = "INSERT INTO pulls_b (exercise_name, num_sets, num_reps, weights, workout_num) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [exercise.exercise_name, exercise.num_sets, exercise.num_reps, exercise.weights, exercise.workout_num]
    results = run_sql(sql, values)
    id = results[0]['id']
    exercise.id = id
    return  exercise

def save_legs(exercise):
    sql = "INSERT INTO legs (exercise_name, num_sets, num_reps, weights, workout_num) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [exercise.exercise_name, exercise.num_sets, exercise.num_reps, exercise.weights, exercise.workout_num]
    results = run_sql(sql, values)
    id = results[0]['id']
    exercise.id = id
    return  exercise







# def save_workout_group_pull_a(exercise):
#     sql = "INSERT INTO pull_a (exercise_name, num_sets, num_reps, weights, workout_group, workout_num, workout_varient) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
#     values = [exercise.exercise_name, exercise.num_sets, exercise.num_reps, exercise.weights, exercise.workout_group, exercise.workout_num, exercise.workout_varient]
#     results = run_sql(sql, values)
#     id = results[0]['id']
#     table.id = id
#     return  table

# def transfer_exercises(table, workout_group, workout_varient):
#     sql = f"INSERT INTO {table} SELECT exercise_name, num_sets, weights FROM exercises WHERE workout_group = {workout_group} AND workout_varient = {workout_varient};"
    
    
    
#     # sql = """
#     #     INSERT INTO %s
#     #     SELECT exercise_name, num_sets, weights FROM exercises
#     #     WHERE workout_group = %s AND workout_varient = %s;
#     # """
#     results = run_sql(sql)



#     CREATE TABLE legs (
#     id SERIAL PRIMARY KEY,
#     exercise_id INT NOT NULL REFERENCES exercise_id(id)
# );
 
    # values = [workout_group, varient]
    # results = run_sql(sql, values)
    # if results:
    #     result = results[0]

    #     workout_test = Workout()
       
    # return workout_test








# class Exercise:
#     def __init__(self, exercise_name, num_sets, num_reps, weight, workout_group, workout_num, workout_varient = "None", id = None):
#         self.exercise_name = exercise_name
#         self.num_sets = num_sets
#         self.num_reps = num_reps
#         self.weight = weight
#         self.workout_group = workout_group
#         self.workout_num = workout_num
#         self.workout_varient = workout_varient
#         self.id = id