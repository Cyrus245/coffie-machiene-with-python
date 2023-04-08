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
            "coffee": 24,
            "milk": 150,

        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100,

        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "coffee": 100,
    "milk": 200,
}

# def test():
#     arr = []
#     for x in MENU:
#         for y in MENU[x]:
#             if y == 'ingredients':
#                 for z in MENU[x][y]:
#                     items = resources[f"{z}"] - MENU["espresso"]["ingredients"][f"{z}"]
#                     arr.append(items)
#                     return arr
#
#
# print(test())
