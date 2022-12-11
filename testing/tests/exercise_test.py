import unittest
from src.exercise import Exercise

class TestExercise(unittest.TestCase):
    
    def setUp(self):
        self.exercise1 = Exercise("Push Up", 3, 8, 0, "Push", 1, "A")


    def test_exercise_has_name(self):
        self.assertEqual("Push Up", self.exercise1.exercise_name)


    def test_exercise_has_reps(self):
        self.assertEqual(8, self.exercise1.num_reps)