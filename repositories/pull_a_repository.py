from db.run_sql import run_sql

from models.pull import Pull
from models.exercise import Exercise
import repositories.exercise_repository as exercise_repository


def select_all():
    pulls_a = []

    sql = "SELECT * FROM pulls_a"
    results = run_sql(sql)

    for row in results:
        exercise = Pull(row['exercise_name'], row['num_sets'], row['num_reps'], row['weights'], row['workout_num'], row['id'])
        pulls_a.append(exercise)
    return pulls_a

