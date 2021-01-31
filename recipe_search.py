import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import webbrowser

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
    }]

def callback(url):
    webbrowser.open_new(url)

root = tk.Tk()

v = tk.StringVar(value='none')


tk.Label(root, 
        text="Choose any dietary restrictions:",
        justify = tk.LEFT,
        padx = 20).pack()

tk.Radiobutton(root, 
               text="None",
               padx = 20, 
               variable=v, 
               value='none').pack(anchor=tk.W)
tk.Radiobutton(root, 
               text="Gluten Free",
               padx = 20, 
               variable=v, 
               value='gluten free').pack(anchor=tk.W)
tk.Radiobutton(root, 
               text="Vegetarian",
               padx = 20, 
               variable=v, 
               value='vegetarian').pack(anchor=tk.W)
tk.Radiobutton(root, 
               text="Vegan",
               padx = 20, 
               variable=v, 
               value='vegan').pack(anchor=tk.W)

def show_recipes():
    print(v.get())
    new_window = Toplevel(root)
    results_list = find_recipes(v.get())
    print(results_list)
    for result in results_list:
        tk.Label(new_window,text=result['title'],
                 font=('Helvetica 14 bold'), fg='blue').pack()
        tk.Label(new_window,text=result['tags'],
                 justify = tk.LEFT).pack()
        link1 = Label(new_window, text="Go to recipe", cursor="hand2")
        link1.pack()
        link1.bind("<Button-1>", lambda e: callback(result['url']))

    
def find_recipes(restriction):
    
    # Create an empty list for results
    results = []

    if restriction == 'none':
        for recipe in recipes:
            results.append(recipe)
        return results
            
    # Loop through the data and match results that fit the requested tag.
    for recipe in recipes:
        print(recipe.get('tags'))
        if restriction in recipe.get('tags'):
            results.append(recipe)
    return results

confirm = tk.Button(root, text ="Find me recipes!", command = show_recipes)

confirm.pack()

root.mainloop()
