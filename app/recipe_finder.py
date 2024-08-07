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
            return ingredients
        print("No meals found.")
        return []
    else:
        print(f"Error: {response.status_code}")



 

# def get_ingredients_from_edamam(dish_name):
#     base_url = 'https://api.edamam.com'
#     search_url = f'{base_url}/search'
#     params = {
#         'q': dish_name,
#         'app_id': EDAMAM_APP_ID,
#         'app_key': EDAMAM_APP_KEY,
#         'from': 0,
#         'to': 1
#     }
#     response = requests.get(search_url, params=params)
#     data = response.json()

#     if data['hits']:
#         recipe = data['hits'][0]['recipe']
#         ingredients = recipe['ingredientLines']
#         return ingredients
#     return []

def get_ingredients(dish_name):
    ingredients = get_ingredients_from_mealdb(dish_name)
    #if not ingredients:
    #    ingredients = get_ingredients_from_edamam(dish_name)
    return ingredients


if __name__ == '__main__':
    dish_name = input('Enter the dish name: ')
    ingredients = get_ingredients(dish_name)
    if ingredients:
        print(f'Ingredients for {dish_name}:')
        for ingredient in ingredients:
            print(f'- {ingredient}')
    else:
        print(f'No ingredients found for {dish_name}.')