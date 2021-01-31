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
    },
    {'id':3,
     'title': 'Lasagna',
     'ingredients': ['ground beef', 'onion', 'spaghetti sauce', 'lasagna noodles',
                     'mozzarella cheese', 'parmesan cheese', 'ricotta cheese'],
     'tags': [],
     'url': 'https://www.pinterest.com/pin/1900024832986490/'
    }]

#Function to open url in a web browser
def callback(url):
    webbrowser.open_new(url)

#Creating the selection window
root = tk.Tk()
root.title('PURA - Pantry Utilizing Recipe App')

v = tk.StringVar(value='none')

tk.Label(root, 
        text="Choose any dietary restrictions:",
        justify = tk.LEFT,
        padx = 20).pack()

#Creating options to restrict the recipe search
#Currently the user can only pick one
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


#Displays filtered recipes in a new window
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

