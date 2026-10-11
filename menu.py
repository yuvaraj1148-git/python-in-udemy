no = int(input('Enter no of items : '))

dish1 = []
dish2 = []
for i in range(no):
    item = input('Enter the item : ')
    price = input('Enter the price : ')

    if item not in dish1:
        dish1.append(item)

    dish2.append(price)

print('--------Menu--------')
for item,price in zip(dish1,dish2):
    dash = 20 - (len(item) + len(price))
    print(f"{item}{'-'*dash}{price}")