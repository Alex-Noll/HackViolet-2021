#import os
import shelve

from flask import Flask, g
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)

api = Api(app)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("recipes.db")
    return db

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    """Present some documentation"""

    # Open the README file
    return "Hello! This is the main page <h1>HELLO<h1>"


class RecipeList(Resource):
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())
        recipes = []

        for key in keys:
            devices.append(shelf[key])
        return {'message': 'Success', 'data': recipes}

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('recipe_title', required=True)
        parser.add_argument('gluten_free', required=True)
        parser.add_argument('vegetarian', required=True)
        parser.addargument('vegan', required=True)

        args = parser.parse_args()

        shelf = get_db()
        shelf[args['identifier']] = args

        return {'message': 'Recipe added', 'data': args}, 201
class Device(Resource):
    def get(self, identifier):
        shelf = get_db()

        if not (identifier in shelf):
            return {'message': 'Recipe not found', 'data': {}}, 404
        return {'message': 'Recipe found', 'data': shelf[identifier]}, 200
    def delete(self, identifier):
        shelf = get_db()
        if not (identifier in shelf):
            return {'message': 'Recipe not found', 'data': {}}, 404
        del shelf[identifier]
        return '', 204

api.add_resource(RecipeList, '/recipes')
api.add_resource(Recipe, '/recipe/<string:identifier>')
