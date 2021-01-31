# HackViolet 2021
## PURA - **Pantry Utilizing Recipe App**
## **Group Members:** *Amber Clauss, Alex Noll, Claire Holmes, & Rose Stanphill*

### Abstract
Our group sought to make an app that could take user input in the form of ingredients and dietary restrictions and produce recipes that used the ingredients that users input and matched the dietary restrictions users selected.

Our goal for the project was to provide filters for:
1. Vegan diets, 
2. Vegetarian diets, 
3. Gluten free diets, 
4. And lastly, diets restricted by budget to represent various minority eating groups. 

Along with these goals, we wanted users to be able to input specific ingredients they already had and wanted to make the app web based on the Google Cloud Platform. These goals we were unable to meet within the time of the competition

### **The Working Code**

Our code makes use of a dictionary of recipes containing arguments for each, specifying if a recipe is vegetarian, vegan, gluten free, or otherwise. Along with this, each entry contains a comprehensive list of all ingredients required and a link to a website containing more information about that recipe.

```python
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
```



 
