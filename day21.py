input_string = '''mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)'''

possible_ingredients = dict()
all_ingredients = list()

for line in input_string.split('\n'):
    ingredients, allergens = line.split(' (')
    ingredient_list = list(ingredients.split())
    all_ingredients.append(ingredient_list)
    for allergen in map(lambda x: x[:-1], allergens.split(' ')[1:]):
        ingredient_set = set(ingredient_list)
        if allergen in possible_ingredients:
            possible_ingredients[allergen].intersection_update(ingredient_set)
        else:
            possible_ingredients[allergen] = ingredient_set

ingredients_with_possible_allergens = set()
for allergen in possible_ingredients:
    ingredients_with_possible_allergens.update(possible_ingredients[allergen])

n = 0
for ingredient_list in all_ingredients:
    for ingredient in ingredient_list:
        if ingredient not in ingredients_with_possible_allergens:
            n += 1

print(n)
