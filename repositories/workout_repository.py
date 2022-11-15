from db.run_sql import run_sql

from models.exercise import Exercise
from models.workout import Workout




def save(workout, workout_name):
    sql = "INSERT INTO workouts (workout_num, workout_name) VALUES (%s, %s) RETURNING *"
    values = [workout.workout_num, workout_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    workout.id = id
    return  workout
