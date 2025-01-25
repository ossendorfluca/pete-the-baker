# Function cakes(), which takes the recipe (object) and the available ingredients (also an object) and returns the maximum number of cakes Pete can bake (integer). 
# For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). 
# Ingredients that are not present in the objects, can be considered as 0.
def cakes(recipe, available):
    # Calculate the maximum number of cakes for each ingredient
    max_cakes = float('inf')  # Start with infinity, find the minimum
    
    for ingredient, amount_needed in recipe.items():
        if ingredient in available:
            # Compute how many cakes can be made with the available amount
            max_cakes = min(max_cakes, available[ingredient] // amount_needed)
        else:
            # If an ingredient is missing, no cakes can be made
            return 0

    return max_cakes