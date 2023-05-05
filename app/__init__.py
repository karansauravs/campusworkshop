"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaablqk728r8866v380-a.oregon-postgres.render.com",
        database="todo_e8iv",
        user="todo_e8iv_user",
        password="aNc5YfRE73VQwbXWLwUpFbaml8z9hshL")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
