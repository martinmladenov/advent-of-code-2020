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

allergens = dict()
while len(allergens) < len(possible_ingredients):
    for allergen in possible_ingredients:
        if len(possible_ingredients[allergen]) != 1:
            continue
        ingredient = possible_ingredients[allergen].pop()
        for other_allergen in possible_ingredients:
            if ingredient in possible_ingredients[other_allergen]:
                possible_ingredients[other_allergen].remove(ingredient)
        allergens[allergen] = ingredient

canonical_dangerous_ingredient_list = list()

for allergen in sorted(allergens):
    canonical_dangerous_ingredient_list.append(allergens[allergen])

print(','.join(canonical_dangerous_ingredient_list))
