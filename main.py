MENU: dict = {
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

profit: float = 0
resources: dict = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients: dict) -> bool:
    """Returns True when order can be made, False if ingredients are insufficient."""
    for ingredient, quantity in order_ingredients.items():
        if quantity > resources[ingredient]:
            print(f"​Sorry there is not enough {ingredient}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name: str, order_ingredients: dict) -> None:
    """
    Deduct the required ingredients from the resources.

    Note: It is assumed that there are enough resources to make the drink
    """
    for ingredient, quantity in order_ingredients.items():
        resources[ingredient] -= quantity
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice: str = input("Type 'off' to exit. Type 'report' to get the report.\n​What would you like "
                        "(espresso/latte/cappuccino)?\n")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink: dict = MENU.get(choice)
        # If the user typed invalid choice for coffee
        if drink is None:
            print(f'Invalid choice')
            break
        if is_resource_sufficient(drink.get('ingredients')):
            payment = process_coins()
            if is_transaction_successful(payment, drink.get('cost')):
                make_coffee(choice, drink.get('ingredients'))
