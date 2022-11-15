DROP TABLE IF EXISTS exercises;
DROP TABLE IF EXISTS workouts;
DROP TABLE IF EXISTS users;
-- DROP TABLE IF EXISTS records;
DROP TABLE IF EXISTS legs;
DROP TABLE IF EXISTS pushes_a;
DROP TABLE IF EXISTS pushes_b;
DROP TABLE IF EXISTS pulls_a;
DROP TABLE IF EXISTS pulls_b;


CREATE TABLE exercises (
  id SERIAL PRIMARY KEY,
  exercise_name VARCHAR(255),
  num_sets INT,
  num_reps INT,
  weights INT,
  workout_group VARCHAR(255),
  workout_num INT,
  workout_varient VARCHAR(255)
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);




-- CREATE TABLE workouts (
--     id SERIAL PRIMARY KEY,
--   
--     user_id INT NOT NULL REFERENCES user_id(id)
--     -- workout_group VARCHAR(255),
--     -- workout_varient VARCHAR(255)
-- );



CREATE TABLE legs (
  id SERIAL PRIMARY KEY,
  exercise_name VARCHAR(255),
  num_sets INT,
  num_reps INT,
  weights INT,
  workout_num INT
);

CREATE TABLE pushes_a (
  id SERIAL PRIMARY KEY,
  exercise_name VARCHAR(255),
  num_sets INT,
  num_reps INT,
  weights INT,
  workout_num INT
);

CREATE TABLE pushes_b (
  id SERIAL PRIMARY KEY,
  exercise_name VARCHAR(255),
  num_sets INT,
  num_reps INT,
  weights INT,
  workout_num INT
);




CREATE TABLE pulls_a (
  id SERIAL PRIMARY KEY,
  exercise_name VARCHAR(255),
  num_sets INT,
  num_reps INT,
  weights INT,
  workout_num INT
);




CREATE TABLE pulls_b (
  id SERIAL PRIMARY KEY,
  exercise_name VARCHAR(255),
  num_sets INT,
  num_reps INT,
  weights INT,
  workout_num INT
);



CREATE TABLE workouts (
    id SERIAL PRIMARY KEY,
    workout_group INT,
    workout_num INT

);


