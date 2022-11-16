from models.exercise import Exercise
from models.user import User
from models.workout import Workout_list
from models.counter import Counter
from repositories import exercise_repository, user_repository


user_1 = User("Lorem", "Ipsum")
user_repository.save(user_1)



exercise_1 = Exercise("Bench Press", 5, 5, 50, "Push", 1, "A")
exercise_2 = Exercise("Overhead Press", 3, 8, 30, "Push", 1, "A")
exercise_3 = Exercise("Incline Dumbell Press", 3, 8, 18, "Push", 1, "A")
exercise_4 = Exercise("Tricep Pushdowns", 3, 8, 25, "Push", 1, "A")
exercise_5 = Exercise("Overhead Tricep Extensions", 3, 8, 18, "Push", 1, "A")
exercise_6 = Exercise("Lateral raises", 3, 15, 8, "Push", 1, "A")

workout_1_push_a_list = [exercise_1, exercise_2, exercise_3, exercise_4, exercise_5, exercise_6]
for exercise in workout_1_push_a_list:
    exercise_repository.save(exercise)
    

exercise_7 = Exercise("Deadlift", 1, 5, 100, "Pull", 2, "A")
exercise_8 = Exercise("Pulldowns", 3, 8, 65, "Pull", 2, "A")
exercise_9 = Exercise("Chest Supported Rows", 3, 8, 75, "Pull", 2, "A")
exercise_10 = Exercise("Face Pulls", 3, 8, 16, "Pull", 2, "A")
exercise_11 = Exercise("Hammer Curls", 3, 8, 12, "Pull", 2, "A")
exercise_12 = Exercise("Dumbell Curls", 3, 8, 12, "Pull", 2, "A")


workout_2_pull_a_list = [exercise_7, exercise_8, exercise_9, exercise_10, exercise_11, exercise_12]
for exercise in workout_2_pull_a_list:
    exercise_repository.save(exercise)


exercise_13 = Exercise("Squats", 5, 5, 65, "Legs", 3, '')
exercise_14 = Exercise("Romanian Deadlift", 3, 8, 70, "Legs", 3, '')
exercise_15 = Exercise("Leg Press", 3, 8, 100, "Legs", 3, '')
exercise_16 = Exercise("Leg Curls", 5, 5, 60, "Legs", 3, '')
exercise_17 = Exercise("Calf Raises", 5, 5, 70, "Legs", 3, '')


workout_3_legs_list = [exercise_13, exercise_14, exercise_15, exercise_16, exercise_17]
for exercise in workout_3_legs_list:
    exercise_repository.save(exercise)

exercise_18 = Exercise("Bench Press", 3, 8, 40, "Push", 4, "B")
exercise_19 = Exercise("Overhead Press", 5, 5, 40, "Push", 4, "B")
exercise_20= Exercise("Incline Dumbell Press", 3, 8, 18, "Push", 4, "B")
exercise_21 = Exercise("Tricep Pushdowns", 3, 8, 25, "Push", 4, "B")
exercise_22 = Exercise("Overhead Tricep Extensions", 3, 8, 18, "Push", 4, "B")
exercise_23 = Exercise("Lateral raises", 3, 15, 8, "Push", 4, "B")


workout_4_push_b_list = [exercise_18, exercise_19, exercise_20, exercise_21, exercise_22, exercise_23]
for exercise in workout_4_push_b_list:
    exercise_repository.save(exercise)


exercise_24 = Exercise("Barbell Rows", 5, 5, 50, "Pull", 5, "B")
exercise_25 = Exercise("Pulldowns", 3, 8, 65, "Pull", 5, "B")
exercise_26 = Exercise("Chest Supported Rows", 3, 8, 75, "Pull", 5, "B")
exercise_27 = Exercise("Face Pulls", 3, 8, 16, "Pull", 5, "B")
exercise_28 = Exercise("Hammer Curls", 3, 8, 12, "Pull", 5, "B")
exercise_29 = Exercise("Dumbell Curls", 3, 8, 12, "Pull", 5, "B")


workout_5_pull_b_list = [exercise_24, exercise_25, exercise_26, exercise_27, exercise_28, exercise_29]

for exercise in workout_5_pull_b_list:
    exercise_repository.save(exercise)
