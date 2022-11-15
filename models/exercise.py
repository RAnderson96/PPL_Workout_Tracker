class Exercise:
    def __init__(self, exercise_name, num_sets, num_reps, weights, workout_group, workout_num, workout_varient = "Normal", id = None):
        self.exercise_name = exercise_name
        self.num_sets = num_sets
        self.num_reps = num_reps
        self.weights = weights
        self.workout_group = workout_group
        self.workout_num = workout_num
        self.workout_varient = workout_varient
        self.id = id

