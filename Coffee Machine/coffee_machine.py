from items import MENU, resources
from art import logo

print(logo)
coin_bank = 0
restart = True
while restart:

    def recipe(coffee):
        """Takes coffee type as an input and deducts the materials required to make it from the resources"""
        resources["water"] -= MENU[coffee]['ingredients']['water']
        if MENU[coffee]['ingredients'] is ['milk']:
            resources["milk"] -= MENU[coffee]['ingredients']['milk']
        resources["coffee"] -= MENU[coffee]['ingredients']['coffee']


    def check_resources(coffee):
        """Checks if there are enough resources available to make coffee."""
        if (MENU[coffee]['ingredients']['water']) > (resources['water']):
            return "Sorry there's not enough water."
        elif MENU[coffee]['ingredients'] is ['milk']:
            if (MENU[coffee]['ingredients']['milk']) > (resources['milk']):
                return "Sorry there's not enough milk."
        elif MENU[coffee]['ingredients']['coffee'] > resources['coffee']:
            return "Sorry there's not enough coffee."


    def cost_processor(coffee, wallet):
        print("Please insert coins.")
        quarters = float(input("How many quarters?"))
        dimes = float(input("How many dimes?"))
        nickles = float(input("How many nickles?"))
        pennies = float(input("How many pennies?"))
        coins = round(0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies, 2)
        if coins == MENU[coffee]['cost']:
            wallet += coins
            return wallet
        elif coins < MENU[coffee]['cost']:
            print("Sorry that's not enough money. Money refunded.")
            return 0
        elif coins > MENU[coffee]['cost']:
            change = round(coins - MENU[coffee]['cost'], 2)
            print(f"Here's your change:  ${change}")
            wallet += MENU[coffee]['cost']
            return wallet


    coffee_options = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee_options == 'off':
        break

    if coffee_options != 'report':
        if check_resources(coffee_options):
            print(check_resources(coffee_options))
            continue
    if coffee_options == 'espresso':
        recipe(coffee_options)
    elif coffee_options == 'latte':
        recipe(coffee_options)
    elif coffee_options == 'cappuccino':
        recipe(coffee_options)

    elif coffee_options == 'report':
        for key, value in resources.items():
            print(f"{key}: {value}ml")
        print(f"Money: ${coin_bank}")
        continue

    coin_bank += (cost_processor(coffee_options, coin_bank))
    if coin_bank != 0:
        print(f"Your {coffee_options} is ready. Enjoy! ☕")
    else:
        break
