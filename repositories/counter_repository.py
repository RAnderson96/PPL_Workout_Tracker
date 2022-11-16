from db.run_sql import run_sql
import pdb
from models.counter import Counter

#self, exercise_id, workout_group_num = 0, id = None
def save(counter):
    sql = "INSERT INTO counters (workout_group_num) VALUES (%s) RETURNING *"
    values = [counter.workout_group_num]
    results = run_sql(sql, values)
    id = results[0]['id']
    counter.id = id
    return  counter

# def update_counter():

   
def update(counter):
    sql = "UPDATE counters SET workout_group_num = %s WHERE id = %s"
    values = [counter.workout_group_num, counter.id]

    result = run_sql(sql, values) 
