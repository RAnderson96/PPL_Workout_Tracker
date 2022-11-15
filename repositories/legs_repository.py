from db.run_sql import run_sql

from models.legs import Leg
from models.exercise import Exercise
import repositories.exercise_repository as exercise_repository


def select_all():
    legs = []

    sql = "SELECT * FROM legs"
    results = run_sql(sql)

    for row in results:
        exercise = Leg(row['exercise_name'], row['num_sets'], row['num_reps'], row['weights'], row['workout_num'], row['id'])
        legs.append(exercise)
    return legs


