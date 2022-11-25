def make_a_dict(file_path):
    with open(file_path, 'rt', encoding='utf-8') as file:
        cook_book = {}
        for line in file:
            dish_name = line.strip()
            ing_count = int(file.readline())
            ing_list = []
            
            for i in range(ing_count):
                ing = file.readline().strip().split(' | ')
                name, quantity, measure = ing
                ingredients = {'ingredient_name': name, 'quantity': quantity, 'measure': measure}
                ing_list.insert(0, ingredients)                
            file.readline()
            cook_book[dish_name] = ing_list                
    return cook_book

def get_shop_list_by_dishes(dishes, persons=int):
    menu = make_a_dict('data.txt')   
    shopping_list = {}   
    for dish in dishes:
        for item in (menu[dish]):                
            items_list = dict([(item['ingredient_name'], {'measure': item['measure'], 'quantity': int(item['quantity'])*persons})])
            if shopping_list.get(item['ingredient_name']):                    
                extra_item = (int(shopping_list[item['ingredient_name']]['quantity']) + int(items_list[item['ingredient_name']]['quantity']))   
                shopping_list[item['ingredient_name']]['quantity'] = extra_item
            else:                    
                shopping_list.update(items_list)

        
    print(shopping_list)
    
get_shop_list_by_dishes(['Утка по-пекински', 'Фахитос'], 9)