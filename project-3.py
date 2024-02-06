ingredient_names = []
original_quantities = []

num_ingredients = int(input("Enter the number of ingredients in the recipe:"))

for i in range(num_ingredients):
    ingredient_names.append(input(f"Enter the name of ingredients in the recipe {i + 1}:"))
    original_quantities.append(float(input(f"Enter the quantity of {ingredient_names[i]}(in grams):")))

num_servings = float(input("Enter the number of servings you want to make:"))

adjusted_quantities = [original_quantity*(num_servings / 1)for original_quantity in original_quantities]

print("\nAdjusted Recipe for", num_servings,"servings:")
for i in range(num_ingredients):
    print(f"{ingredient_names[i]} - {adjusted_quantities[i]:.2f} grams")