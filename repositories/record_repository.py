from db.run_sql import run_sql
import pdb
from models.exercise import Exercise
from models.workout import Workout_list
from models.record import Record



def save(record):
    sql = "INSERT INTO records (exercise_id, workout_dict) VALUES (%s, %s) RETURNING *"

    values = [record.exercise.id, record.workout_dict]
    results = run_sql(sql, values)
    
    id = results[0]['id']
    record.id = id
    return  record



# def save(book):
#     sql = "INSERT INTO books (title, genre, publisher, author_id) VALUES (%s, %s, %s, %s) RETURNING *"
#     values = [book.title, book.genre, book.publisher, book.author.id]
#     results = run_sql(sql, values)
#     id = results[0]['id']
#     book.id = id
#     return book