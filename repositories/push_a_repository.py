from db.run_sql import run_sql

from models.push import Push
from models.exercise import Exercise
import repositories.exercise_repository as exercise_repository


def select_all():
    pushes_a = []

    sql = "SELECT * FROM pushes_a"
    results = run_sql(sql)

    for row in results:
        exercise = Push(row['exercise_name'], row['num_sets'], row['num_reps'], row['weights'], row['workout_num'], row['id'])
        pushes_a.append(exercise)
    return pushes_a