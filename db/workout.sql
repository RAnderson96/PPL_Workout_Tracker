DROP TABLE IF EXISTS exercises;
DROP TABLE IF EXISTS workouts;

CREATE TABLE exercises (
  id SERIAL PRIMARY KEY,
  exercise_name VARCHAR(255),
  num_sets INT,
  num_reps INT,
  weight FLOAT,
  workout_group VARCHAR(255),
  workout_num INT,
  workout_varient VARCHAR(255)
);

-- exercise_name, num_sets, num_reps, weight, workout_group, workout_num, workout_varient = "None", exercise_id = None):
-- self, workout_record, legs_id = None):

-- (self, exercise, user, id = None):
CREATE TABLE workouts (
    id SERIAL PRIMARY KEY,
    exercise_id 

)




CREATE TABLE records (
    id SERIAL PRIMARY KEY,
    workout_id INT NOT NULL REFERENCES workout_id(id)
)




CREATE TABLE legs (
    id SERIAL PRIMARY KEY,
    record_id INT NOT NULL REFERENCES record_id(id)
)

CREATE TABLE pushes (
    id SERIAL PRIMARY KEY,
    record_id INT NOT NULL REFERENCES record_id(id)
)

CREATE TABLE pulls (
    id SERIAL PRIMARY KEY,
    record_id INT NOT NULL REFERENCES record_id(id)
)


-- def __init__(self, workout_id, workout, id = None):



CREATE TABLE books (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  author_id INT NOT NULL REFERENCES authors(id),
  genre VARCHAR(255)
);