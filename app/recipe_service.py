import requests

# Get dish name
def get_ingredients_from_mealdb(dish_name):
    
    #Search meal by name: www.themealdb.com/api/json/v1/1/search.php?s=Arrabiata
    base_url = 'https://www.themealdb.com/api/json/v1/1'
    search_url = f'{base_url}/search.php?s={dish_name}'
    
    # Request data 
    response = requests.get(search_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Check if the response contains meals
        if data['meals']:
            meal = data['meals'][0]
            ingredients = []
            for i in range(1, 21):  # The API allows up to 20 ingredients
                ingredient = meal.get(f'strIngredient{i}')
                measure = meal.get(f'strMeasure{i}')
                if ingredient and measure:
                    ingredients.append(f'{ingredient} ({measure})')
            print("it comes from the mealdb")
            return ingredients
        print("No meals found with mealdb.")
        return []
    else:
        print(f"Error: {response.status_code}")



 

def get_ingredients_from_edamam(dish_name):
 # Define the base URL and parameters
    url = "https://api.edamam.com/api/recipes/v2"
    params = {
        "type": "public",  # Specifies the type of recipes
        "q": dish_name,     # The search query (e.g., "chicken")
        "app_id": "88c9c080",  # Your Edamam API app_id
        "app_key": "0f7e14c7ab64a3fa0624f48bf68f8a29" # Your Edamam API app_key
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        
        # Initialize a list to hold the ingredients
        ingredients = []
        for recipe in data.get('hits', []):
            recipe_ingredients = recipe['recipe']['ingredients']

            for ingredient in recipe_ingredients:
                ingredients.append({
                    'text': ingredient.get('text'),
                    'quantity': ingredient.get('quantity'),
                    'measure': ingredient.get('measure'),
                    'food': ingredient.get('food'),
                    'weight': ingredient.get('weight'),
                })

        return ingredients
    return []

def get_ingredients(dish_name):
    ingredients = get_ingredients_from_mealdb(dish_name)
    if not ingredients:
        ingredients = get_ingredients_from_edamam(dish_name)
    return ingredients