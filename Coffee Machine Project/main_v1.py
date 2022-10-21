MENU = {
    "expresso": {
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

# print report

# check if resources are sufficient?

# process coins

# check transaction successful

# make coffee

drinks = list(MENU.keys())
balance = 0
expresso_water = MENU["expresso"]["ingredients"]["water"]
expresso_coffee = MENU["expresso"]["ingredients"]["coffee"]
latte_water = MENU["latte"]["ingredients"]["water"]
latte_milk = MENU["latte"]["ingredients"]["milk"]
latte_coffee = MENU["latte"]["ingredients"]["coffee"]
cappuccino_water = MENU["cappuccino"]["ingredients"]["water"]
cappuccino_milk = MENU["cappuccino"]["ingredients"]["milk"]
cappuccino_coffee = MENU["cappuccino"]["ingredients"]["coffee"]
total_water = resources["water"]
total_milk = resources["milk"]
total_coffee = resources["coffee"]
payment=0


def report():
  print(f"Water: {total_water}ml")
  print(f"Milk: {total_milk}ml")
  print(f"Coffee: {total_coffee}g")
  print(f"Money: ${payment}")

def check_resources(option, total_water, total_coffee, total_milk):
    if option == "expresso" and total_water >= expresso_water and total_coffee >= expresso_coffee:
        return True
    elif option == "latte" and total_water >= latte_water and total_coffee >= latte_coffee and total_milk >= latte_milk:
        return True
    elif option == "cappuccino" and total_water >= cappuccino_water and total_coffee >= cappuccino_coffee and total_milk >= cappuccino_milk:
        return True
    else:
        if total_water < expresso_water or total_water < latte_water or total_water < cappuccino_water:
            return False
        elif total_coffee < expresso_coffee or total_coffee < latte_coffee or total_coffee < cappuccino_coffee:
            return False
        else:
            return False


def check_payment(payment, option):
    if option == "expresso" and payment >= MENU["expresso"]["cost"]:
        balance = payment - MENU["expresso"]["cost"]
        print(f"Here is your ${balance} in change.")
        print("Here is your expresso. Enjoy!")
    elif option == "latte" and payment >= MENU["latte"]["cost"]:
        balance = payment - MENU["latte"]["cost"]
        print(f"Here is your ${balance} in change.")
        print("Here is your latte. Enjoy!")
    elif option == "cappuccino" and payment >= MENU["cappuccino"]["cost"]:
        balance = payment - MENU["cappuccino"]["cost"]
        print(f"Here is your ${balance} in change.")
        print("Here is your cappuccino. Enjoy!")
    else:
        print("Not enough money")


def insert_coins():
    print("Please insert coins.")

    quarters = 0
    dimes = 0
    nickles = 0
    pennies = 0
    while type(quarters):
        quarters = float(input("how many quarters?: ")) * 25
        dimes = float(input("how many dimes?: ")) * 10
        nickles = float(input("how many nickles?: ")) * 5
        pennies = float(input("how many pennies?: "))
        break

    total_in_dollars = (quarters + dimes + nickles + pennies) / 100
    return total_in_dollars


option = "expresso"
while option in drinks:
    option = input("What would you like? (expresso/latte/cappuccino): ")
    if option=="report":
      report()

    if option not in drinks and option!="report":
        print("Invalid option")
        break

    if check_resources(option, total_water, total_coffee, total_milk) == True:
      if option=="expresso":
        total_water -= expresso_water
        total_coffee -= expresso_coffee
      elif check_resources(option, total_water, total_coffee, total_milk) == True and option=="latte":
        total_water -= expresso_water
        total_coffee -= expresso_coffee
        total_milk -= latte_milk
      else:
        total_water -= expresso_water
        total_coffee -= expresso_coffee
        total_milk -= latte_milk
    else:
      if total_water < expresso_water or total_water < latte_water or total_water < cappuccino_water:
        print("Not enough water")
        continue
      elif total_coffee < expresso_coffee or total_coffee < latte_coffee or total_coffee < cappuccino_coffee:
        print("Not enough coffee")
        continue
      else:
        print("Not enough milk")
        continue



    payment = float(insert_coins())
    check_payment(payment, option)




