from flask import Blueprint, request, jsonify
from app.recipe_service import get_ingredients

# Create a blueprint for the main routes
main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/ingredients', methods=['GET'])
def ingredients():
    dish_name = request.args.get('dish')
    
    if not dish_name:
        return jsonify({'error': 'Dish name is required'}), 400
    
    ingredients = get_ingredients(dish_name)
    
    if ingredients:
        return jsonify({'dish': dish_name, 'ingredients': ingredients})
    else:
        return jsonify({'error': 'No ingredients found for the dish'}), 404
