from db.run_sql import run_sql

from models.exercise import Exercise
from models.workout import Workout


def save(exercise):
    sql = "INSERT INTO exercises (author_name) VALUES (%s) RETURNING *"
    values = [author.author_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    author.id = id
    return author