phones = [{'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
          {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
          {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
          ]

sold = []
def main():
    for phone in phones:
        print(f'Сумарное кол-во продаж,', phone['product'], ':', sum(phone['items_sold']))
        print(f'Среднее кол-во продаж,', phone['product'], ':', sum(phone['items_sold']) / len(phone['items_sold']))
for i in phones:
    sold += i['items_sold']
sold_sum = sum(sold)
sold_num = len(sold)
print('Сумарное кол-во всех телефонов:', sold_sum)
print('Среднее кол-во продаж всех телефонов:', sold_sum / sold_num)

if __name__ == "__main__":
    main()



