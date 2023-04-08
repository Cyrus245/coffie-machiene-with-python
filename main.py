# TODO 1:Print report.

from data import MENU, resources


def resource_sufficient(chosen):
    for item in chosen:
        if chosen[item] > resources[item]:
            print(f"sorry there isn't enough {item}")
            return False
    return True


def money_count():
    """calculating the money"""
    print("Please insert coins.")
    total = int(input("How many quarters?")) * 0.25
    total += int(input("How many dimes?")) * 0.10
    total += int(input("How many nickles?")) * 0.05
    total += int(input("How many pennies?")) * 0.01
    return total


def material_count(chosen_item, chosen_item_ingredients):
    """calculating the existing resources"""
    for item in chosen_item_ingredients:
        resources[item] -= chosen_item_ingredients[item]
    print(f"Here is your {chosen_item}☕️.Enjoy!")


def coffee_machine():
    """it's a virtual coffee machine."""
    on = True
    money = 0
    while on:
        coffee_criteria = input("What would you like? (espresso/latte/cappuccino):").lower()
        if coffee_criteria == 'off':
            on = False
        elif coffee_criteria == 'report':
            """if input == report show report"""
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${money}")
        else:
            chosen_item = MENU[coffee_criteria]
            result = resource_sufficient(chosen_item["ingredients"])
            if result:
                if coffee_criteria in MENU:
                    """if user selected category is in the menu """
                    money_received = money_count()
                    if money_received >= chosen_item["cost"]:
                        drinks_cost = chosen_item["cost"]
                        change = money_received - drinks_cost
                        print(f"Here is {round(change, 2)}$ change.")
                        money += drinks_cost
                        material_count(coffee_criteria, chosen_item["ingredients"])

                    else:
                        """if user input less amount than a price of desired coffee"""
                        on = False
                        print("Sorry that's not enough money.Money refunded")

                else:
                    print("Type right choice")


coffee_machine()
