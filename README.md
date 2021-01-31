# HackViolet 2021
## PURA - **Pantry Utilizing Recipe App**
## **Group Members:** *Amber Clauss, Alex Noll, Claire Holmes, & Rose Stanphill*

### Abstract
Our group sought to make an app that could take user input in the form of ingredients and dietary restrictions and produce recipes that used the ingredients that users input and matched the dietary restrictions users selected.
#### Our Goal
Our goal for the project was to provide filters for:
1. Vegan diets, 
2. Vegetarian diets, 
3. Gluten free diets, 
4. And lastly, diets restricted by budget to represent various minority eating groups. 

Along with these goals, we wanted users to be able to input specific ingredients they already had and wanted to make the app web based on the Google Cloud Platform. These goals we were unable to meet within the time of the competition

#### Stakeholders
Stakeholders for this app include but are not limited to: organic grocery stores, restaurants, and low-income households. The intent of this program is to provide this demographic with the opportunity of healthy eating, while minimizing the hassle and cost of their dietary restrictions. 


### **The Working Code**

Our code makes use of a dictionary of recipes containing arguments for each, an identifier for each recipe, and then arguments specifying if a recipe is vegetarian, vegan, gluten free, or otherwise. Along with this, each entry contains a comprehensive list of all ingredients required and a link to a website containing more information about that recipe. 
Dictionary code block shown below:
```python
#A list of dictionaries that represent recipes
recipes = [
    {'id': 0,
     'title': 'Gluten Free Waffles',
     'ingredients': ['eggs', 'baking flour(gluten free)', 'baking soda',
                     'salt', 'sugar', 'vanilla extract', 'butter', 'milk'],
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
     'tags': ['vegan'],
     'url': 'https://themodernproper.com/walnut-and-lentil-bolognese'
    },
    {'id':3,
     'title': 'Lasagna',
     'ingredients': ['ground beef', 'onion', 'spaghetti sauce', 'lasagna noodles',
                     'mozzarella cheese', 'parmesan cheese', 'ricotta cheese'],
     'tags': [],
     'url': 'https://www.pinterest.com/pin/1900024832986490/'
    }]
```

#### **The Interface**

Along with our dictionary, we made our GUI using tkinter, we made use of radial buttons, meaning that in our current build users cannot select multiple filters (ie, gluten free AND vegetarian). The GUI, based on what filter the user selects, displays recipes fitting the requirements as shown in the code block below:
```python
def show_recipes():
    #Creates a new window with the title 'Recipes'
    new_window = Toplevel(root)
    new_window.title('Recipes')
    #Returns the list of recipes to be displayed
    results_list = find_recipes(v.get())
    
    #Loops through the results list and prints them in the new window
    for result in results_list:
        
        tk.Label(new_window,text=result['title'],
                 font=('Times 14 bold'), fg='blue').pack()
        #If there are no tags, indicate it does not fit any of the available restrictions
        if len(result['tags']) == 0:
            tk.Label(new_window,text='Does not fit and dietary restrictions',
                 font=('Times 12')).pack()
        else:
            tk.Label(new_window,text=result['tags'],
                 font=('Times 12')).pack()
        #Clickable link to go to the webpage for the recipe
        link1 = Label(new_window, text="Go to recipe",
                      font=('Times 12'), cursor="hand2")
        link1.pack()
        link1.bind("<Button-1>", lambda e: callback(result['url']))

    
#Finds recipes based on dietary restrictions
def find_recipes(restriction):
    # Create an empty list for results
    results = []

    #If there are no restrictions, show everything
    if restriction == 'none':
        for recipe in recipes:
            results.append(recipe)
        return results
            
    # Loop through the data and match results that fit the restriction
    for recipe in recipes:
        print(recipe.get('tags'))
        if restriction in recipe.get('tags'):
            results.append(recipe)
    return results

#Button that opens a new window and displays results
confirm = tk.Button(root, text ="Find me recipes!", command = show_recipes)

confirm.pack()

root.mainloop()
```

### **The non-working/unfinished code**
As mentioned earlier in the abstract, our group sought to make a web-based API on the Google Cloud Platform, we set up a VM instance in the compute engine, and made the beginnings of a web-based API using pycharm. Our web-based API makes use of a database as opposed to a dictionary. We were able to get working GET & POST requests to and from our webAPI on a locally-running instance, but did not have enough time to implement this on our VM on the Google Cloud Platform
Our webAPI code is shown below:
```python
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
```


 
