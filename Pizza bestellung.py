

def pizza_order():
    print("Welcome to the Pizza Delivery Program!")

    size = input(f"What size pizza would you like to order? (S, M, L):\n")

    if size == 'S':
        base_price = 10
    elif size == 'M':
        base_price = 15
    elif size == 'L':
        base_price = 20
    else:
        print("Invalid input! Please choose a valid size (S, M, or L).")
        return

    pepperoni = input(f"Would you like to add some pepperoni? (Y or N):\n")
    if pepperoni == 'y':
        if size == 'S':
            base_price += 2
        else:
            base_price += 3

    extra_cheese = input(f"Would you like to add some cheese? (Y or N):\n")
    if extra_cheese == 'y':
        base_price += 1

    print(f"The total price for your pizza is: ${base_price}")

pizza_order()



































