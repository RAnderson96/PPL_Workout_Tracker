from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.exercise import Exercise
import repositories.exercise_repository as exercise_repository
import repositories.workout_repository as workout_repository

exercise_blueprint = Blueprint("exercise", __name__)