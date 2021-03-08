def move_variables(self, items):
    # can you find all the bad code here?
    # refactor it to a better solution
    price = 0
    max_level = 5
    number_of_items = 17

    # Need to print out items with price

    # calculate total price
    for i in range(number_of_items):
        line_number = i
        item_spacer = 5
        price += items[i]
        print('Item', line_number, " " * item_spacer, price)

    print('Total price is', price)
