import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

recipes = [
    {'id': 0,
     'title': 'Gluten Free Waffles',
     'ingredients': ['eggs', 'baking flour(gluten free)',
                     'baking soda', 'salt', 'sugar', 'vanilla extract', 'butter', 'milk'],
     'tags': ['gluten free', 'vegetarian'],
     'url': 'https://www.pinterest.com/pin/5559199530451854/'
    },
    {'id': 1,
     'title': "Easy Lentil Shepherd's Pie",
     'ingredients': ['brown lentils', 'vegetable broth', 'olive oil', 'onion',
                     'mushrooms', 'carrot', 'celery', 'frozen peas', 'flour',
                     'red wine', 'vegan worcestershire sauce', 'tomato paste',
                     'parsley', 'salt', 'pepper', 'mashed potatoes'],
     'tags': ['vegetarian', 'vegan'],
     'url': 'https://www.spendwithpennies.com/easy-lentil-shepherds-pie-vegetarian/' 
    },
    {'id': 2,
     'title': 'Walnut and Lentil Bolognese',
     'ingredients': ['olive oil', 'carrots', 'celery', 'onion', 'walnuts',
                     'lentils', 'marinara sauce', 'pasta'],
     'url': 'https://themodernproper.com/walnut-and-lentil-bolognese'
    }]


@app.route('/', methods=['GET'])
def home():
    return "<h1>Recipe Search</h1><p>This site is a prototype API for a recipe searching program.</p>"

@app.route('/api/v1/resources/recipes/all', methods=['GET'])
def api_all():
    return jsonify(recipes)

@app.route('/api/v1/resources/recipes', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for recipe in recipes:
        if recipe['id'] == id:
            results.append(recipe)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

app.run()