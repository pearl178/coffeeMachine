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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def order():
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\n"
              f"Coffee: {resources['coffee']}g\nMoney: ${resources['money']}")
    elif order == "off":
        global is_on
        is_on = False
    else:
        if is_ingredients_enough(MENU[order]["ingredients"]):
            payment_process(order)


def is_ingredients_enough(ingredients):
    """Returns True if there is enough ingredients to make the order. And False if there are enough ingredients."""
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry. There's not enough {item}.")
            return False
    return True


def payment_process(order):
    """Process coins inserted, check they are enough, and calculate the change."""
    print("Please insert coins.")
    total = int(input("How many quarters?: "))*0.25
    total += int(input("How many dimes?: "))*0.1
    total += int(input("How many nickles?: "))*0.05
    total += int(input("How many pennies?: "))*0.01
    price = MENU[order]["cost"]
    if total >= price:
        change = round(total - price, 2)
        resources["money"] += price
        ingredients_deduction(order)
        print(f"Here is ${change} in change.\nHere is your {order}☕. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")


def ingredients_deduction(order):
    """Deduct the amount of required ingredients from the resources."""
    for item in MENU[order]["ingredients"]:
        resources[item] -= MENU[order]["ingredients"][item]


resources["money"] = 0
is_on = True
while is_on:
    order()
