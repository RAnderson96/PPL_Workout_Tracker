from db.run_sql import run_sql

from models.user import User

def save(user):
    sql = "INSERT INTO users (first_name, last_name) VALUES (%s, %s) RETURNING *"
    values = [user.first_name, user.last_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    user.id = id
    return  user



def select_all():
    users = []

    sql = "SELECT * FROM users"
    results = run_sql(sql)

    for row in results:
        # exercise = exercise_repository.select(row['exercise_id'])
        record = User(row['first_name'], row['last_name'], row['id'])
        users.append(record)
    return users