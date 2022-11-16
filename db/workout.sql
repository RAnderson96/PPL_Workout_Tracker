
DROP TABLE IF EXISTS exercises CASCADE;
DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS counters CASCADE;
DROP TABLE IF EXISTS records CASCADE;





CREATE TABLE exercises (
  id SERIAL PRIMARY KEY,
  exercise_name VARCHAR(255),
  num_sets INT,
  num_reps INT,
  weights FLOAT,
  workout_group VARCHAR(255),
  workout_num INT,
  workout_varient VARCHAR(255)
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);

CREATE TABLE counters (
  id SERIAL PRIMARY KEY,
  -- exercise_id INT NOT NULL REFERENCES exercises(id),
  workout_group_num INT
);

CREATE TABLE records (
  id SERIAL PRIMARY KEY,
  workout_dict TEXT[],
  exercise_id INT NOT NULL REFERENCES exercises(id),
  time_created TIMESTAMP DEFAULT NOW()

);


