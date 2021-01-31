#HackViolet 2021

# Recipe Filtering Service

## Usage

All responses will have the form

```json
{
    "data": "String or integer value",
    "message": "Successful/Not Successful"
}
```

Subsequent response definitions will only detail the expected value of the `data field`

### List all recipes

**Definition**

`GET /recipes`

**Response**

- `200 OK` on success

```json
[
    {
        "recipe_title": "Chicken Nuggies",
        "gluten_free": "No",
        "vegetarian": "No",
        "vegan": "No"
    },
    {
        "recipe_title": "Choccy Milk",
        "gluten_free": "Yes",
        "vegetarian": "Yes",
        "vegan": "No"
    }
]
```

### Registering a new recipe

**Definition**

`POST /recipes`

**Arguments**

- `"recipe_title":string` a unique name for this recipe
- `"gluten_free":string` if this recipe is gluten free
- `"vegetarian":string` if this recipe is vegetarian
- `"vegan":string` if this recipe is vegan

If a recipe with the given recipe title already exists, the existing recipe will be overwritten.

**Response**

- `201 Created` on success

```json
{
    "recipe_title": "Mac and Cheese",
    "gluten_free": "No",
    "vegetarian": "No",
    "vegan": "No"
}
```

## Lookup recipe details

`GET /recipe/<recipe_title>`

**Response**

- `404 Not Found` if the recipe does not exist
- `200 OK` on success

```json
{
    "recipe_title": "Mac and Cheese",
    "gluten_free": "No",
    "vegetarian": "No",
    "vegan": "No"
}
```

## Delete a recipe

**Definition**

`DELETE /recipes/<recipe_title>`

**Response**

- `404 Not Found` if the recipe does not exist
- `204 No Content` on success
