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

print(f' \n')


# Задача №2
def get_shop_list_by_dishes(dishes, person_count):
  list_of_ingredients_and_quantities = {}
  
  # Проходим по каждому блюду из списка
  for dish in dishes:
    # Проверка, существует ли блюдо в cook_book
    if dish in cook_book:
      # Проходим по каждому ингредиенту блюда
      for ingredient in cook_book[dish]:
        ingredient_name = ingredient['ingredient_name']
        quantity = ingredient['quantity'] * person_count
        measure = ingredient['measure']
        # Проверка если ингредиент есть в списке, увеличиваем количество
        if ingredient_name in list_of_ingredients_and_quantities:
          list_of_ingredients_and_quantities[ingredient_name]['quantity'] += quantity
        else:
          # Проверка если ингредиента еще нет в списке, добавляем его
          list_of_ingredients_and_quantities[ingredient_name] = {
            'measure': measure,
            'quantity': quantity
          }
    else:
      print(f"Внимание!: '{dish}' блюдо отсутствует в cook_book.")
  
  # Определение порядка вывода списка ингредиентов
  desired_order = ['Картофель', 'Молоко', 'Помидор', 'Сыр гауда', 'Яйцо', 'Чеснок']
  
  # Форматированная печать в установленном порядке
  for ingredient in desired_order:
    if ingredient in list_of_ingredients_and_quantities:
      info = list_of_ingredients_and_quantities[ingredient]
      print(f"'{ingredient}': {{'measure': '{info['measure']}', 'quantity': {info['quantity']}}}")


# Вызов функции по примеру
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

print(f' \n')