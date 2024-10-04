# Чтение данных из файла
def read_recipes(file_name):
  with open('recipes.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    n = 0
    while True:
      dish_name = file.readline().strip()
      n += 1
      # Выход из цикла когда в файле закончились строки или когда прочитаны рецепты первых 3 блюд
      if not dish_name or n == 4:
          break
      
      num_ingredients = int(file.readline().strip())
      
      # Создание списока ингредиентов
      ingredients = []
      for _ in range(num_ingredients):
        ingredient_line = file.readline().strip()
        ingredient_name, quantity, measure = ingredient_line.split(' | ')
        
        # Добавление ингредиента в список
        ingredients.append({
          'ingredient_name': ingredient_name,
          'quantity': int(quantity),
          'measure': measure
        })
      
      # Добавление блюда и его ингредиенты в словарь cook_book
      cook_book[dish_name] = ingredients
    
      file.readline()
  
  return cook_book


# Функция - чтение файла и вывод cook_book
cook_book = read_recipes('recipes.txt')
for dish, ingredients in cook_book.items():
  print(f'{dish}:')
  for ingredient in ingredients:
    print(' ', ingredient)

# Вывод структуры словаря cook_book
# print(cook_book)