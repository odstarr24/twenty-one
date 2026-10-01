




MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}



def mechanics():
    i = 1
    while i>0:
        type = input("what type of coffee would you like?(latte/cappuccino/espresso) type no to end the process\n")

        cash = 0
        cappuccino_price = 3.0
        espresso_price = 1.50
        latte_price = 2.50

        if type not in MENU:
            print("process finished")



        if type in MENU:
            print("throw in some coins, please.")
            penny = int(input("how many pennies?\n"))
            cash += penny * 0.01
            dime = int(input("how many dimes?\n"))
            cash += dime * 0.10
            nickel = int(input("how many nickel?\n"))
            cash += nickel * 0.05
            quarter = int(input("how many quarters?\n"))
            cash += quarter * 0.25



        if type == "cappuccino" and cash >= cappuccino_price:
                if resources["water"] >= 250:
                    if resources["milk"] >= 100:
                        if resources["coffee"] >= 24:
                            print(f"alright, here you go! excess cash was refunded.({cash})")
                            cash == 0
                            resources["water"] -= 250
                            resources["milk"] -= 100
                            resources["coffee"] -= 24
                            print(f"water = {resources['water']}, milk = {resources['milk']}, coffee = {resources['coffee']}")



        elif type == "cappuccino" and cash < cappuccino_price:
            print(f"you inserted ${cash}. the cappuccino costs {cappuccino_price}")

        elif type == "cappuccino" and cash >= cappuccino_price:
            if resources["water"] < 250:
                print("please refill the water.")

        elif type == "cappuccino" and cash >= cappuccino_price:
            if resources["milk"] < 100:
                print("please refill the milk.")

        elif type == "cappuccino" and cash >= cappuccino_price:
            if resources["coffee"] < 24:
                print("please refill the coffee.")


        elif type == "espresso" and cash >= espresso_price:
                if resources["water"] >= 50:
                    if resources["milk"] >= 0:
                        if resources["coffee"] >= 18:
                            print(f"alright, here you go! excess cash was refunded.({cash})")
                            cash == 0
                            resources["water"] -= 50
                            resources["milk"] -= 0
                            resources["coffee"] -= 18
                            print(f"water = {resources['water']}, milk = {resources['milk']}, coffee = {resources['coffee']}")


        elif type == "espresso" and cash < espresso_price:
            print(f"you inserted {cash}. the espresso costs {espresso_price}")

        elif type == "espresso" and cash >= espresso_price:
            if resources["water"] < 50:
                print("please refill the water")

        elif type == "espresso" and cash >= espresso_price:
            if resources["coffee"] < 18:
                print("please refill the coffee")



        elif type == "latte" and cash >= latte_price:
                if resources["water"] >= 200:
                    if resources["milk"] >= 150:
                        if resources["coffee"] >= 24:
                            print(f"alright, here you go! excess cash as refunded.({cash})")
                            cash == 0
                            resources["water"] -= 200
                            resources["milk"] -= 150
                            resources["coffee"] -= 24
                            print(f"water = {resources['water']}, milk = {resources['milk']}, coffee = {resources['coffee']}")


        elif type == "latte" and cash < latte_price:
            print(f"you inserted ${cash}. the latte costs {latte_price}")

        elif type == "latte" and cash >= latte_price:
            if resources["water"] < 200:
                print("please refill the water.")

        elif type == "latte" and cash >= latte_price:
            if resources["milk"] < 150:
                print("please refill the milk.")

        elif type == "latte" and cash >= latte_price:
            if resources["coffee"] < 24:
                print("please refill the coffee.")

        elif type == "no":
            i=0
            print("ending process")

mechanics()



