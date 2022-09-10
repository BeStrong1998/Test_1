"""
Домашнее задание №1
Цикл for: Продажи товаров
* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
list = [{'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
]
def main():
    iPhone12 = 0
    for i in list[0]['items_sold']:
        iPhone12 += i
    print('Сумма продаж товара iPhone 12 :', iPhone12)
    print('Средняя сумма продаж iPhone 12:', iPhone12 / len(list[0]['items_sold']))
    print()

    XiaomiMi11 = 0
    for j in list[1]['items_sold']:
        XiaomiMi11 += j
    print('Сумма продаж товара Xiaomi Mi11', XiaomiMi11)
    print('Средняя сумма продаж Xiaomi Mi11:', XiaomiMi11 / len(list[1]['items_sold']))
    print()

    SamsungGalaxy21 = 0
    for k in list[2]['items_sold']:
        SamsungGalaxy21 += k
    print('Сумма продаж товара Samsung Galaxy 21', SamsungGalaxy21)
    print('Средняя сумма продаж Samsung Galaxy 21:', SamsungGalaxy21 / len(list[2]['items_sold']))
    print()

    sum = iPhone12 + XiaomiMi11 + SamsungGalaxy21
    print('Сумма всех товаров iPhone 12, Xiaomi Mi11, Samsung Galaxy 21:', sum)
    print()

    average_sum = sum / len(list)
    print('Средняя сумма всех товаров iPhone 12, Xiaomi Mi11, Samsung Galaxy 21:', average_sum)
    
if __name__ == "__main__":
    main()
    