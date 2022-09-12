phones = [{'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
        {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
        {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
        ]

def main():
    for phone in phones:
        print(f'Сумарное кол-во продаж:', phone['product'], ':', sum(phone['items_sold']))
        print(f'Среднее кол-во продаж:', phone['product'], ':', sum(phone['items_sold']) / len(phone['items_sold']))

print(f'Сумарное кол-во продаж всех телефонов:', sum(phones[0]['items_sold'] + phones[1]['items_sold'] + phones[2]['items_sold']))
print(f'Среднее кол-во продаж всех телефонов:', sum(phones[0]['items_sold'] + phones[1]['items_sold'] + phones[2]['items_sold']) / len(phones[0]['items_sold'] + phones[1]['items_sold'] + phones[2]['items_sold']))

if __name__ == "__main__":
    main()

    