from db.run_sql import run_sql

from models.exercise import Exercise
from models.workout import Workout


# CREATE TABLE workouts (
#     id SERIAL PRIMARY KEY,
#     exercise_id INT NOT NULL REFERENCES exercise_id(id),
#     user_id INT NOT NULL REFERENCES user_id(id),
# );


# CREATE TABLE workouts (
#     id SERIAL PRIMARY KEY,
#     exercise_id INT NOT NULL REFERENCES exercise_id(id),
    
# );

# self, workout_group, workout_name, id = None):

def save(workout, workout_name):
    sql = "INSERT INTO workouts (workout_num, workout_name) VALUES (%s, %s) RETURNING *"
    values = [workout.workout_num, workout_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    workout.id = id
    return  workout
