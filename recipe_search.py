import tkinter as tk

root = tk.Tk()

v = tk.IntVar()

tk.Label(root, 
        text="Choose any dietary restrictions:",
        justify = tk.LEFT,
        padx = 20).pack()

tk.Radiobutton(root, 
               text="None",
               padx = 20, 
               variable=v, 
               value=1).pack(anchor=tk.W)
tk.Radiobutton(root, 
               text="Gluten Free",
               padx = 20, 
               variable=v, 
               value=2).pack(anchor=tk.W)
tk.Radiobutton(root, 
               text="Vegetarian",
               padx = 20, 
               variable=v, 
               value=3).pack(anchor=tk.W)
tk.Radiobutton(root, 
               text="Vegan",
               padx = 20, 
               variable=v, 
               value=4).pack(anchor=tk.W)

def show_recipes():
    top2 = TopLevel()
    top2.mainloop()
   #tkMessageBox.showinfo( "Hello Python", "Hello World")

confirm = tk.Button(root, text ="Find me recipes!", command = show_recipes)

confirm.pack()

root.mainloop()

print(v.get())


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
    }]


#@app.route('/api/v1/resources/recipes', methods=['GET'])
def api_id():
    # Check if a tag was provided as part of the URL.
    # If tag is provided, assign it to a variable.
    # If no ID is provided, display all recipes.
    if 'tag' in request.args:
        tag = request.args['tag']
    else:
        return jsonify(recipes)

    # Create an empty list for results
    results = []

    # Loop through the data and match results that fit the requested tag.
    for recipe in recipes:
        print(recipe.get('tags'))
        if tag in recipe.get('tags'):
            results.append(recipe)

    # Use the jsonify function from Flask to convert list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

#app.run()