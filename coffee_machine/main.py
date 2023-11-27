# Coffee Machine Program Requirements
from menu import MENU, resources


def check_resource(u, m, r):
    """Checks if the resources required to make the coffee option are sufficient or not.
    Returns the balance after deducting the required amount from stock balance"""
    balance = 0
    b = m[u]['ingredients']
    for i in r:
        if i in b:
            if r[i] > b[i]:
                balance = 1
            else:
                balance = i
                return balance
    return balance


power_status = True
money = 0

# 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”

# a. Check the user’s input to decide what to do next.

# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.
while power_status:
    user_request = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # 2. Turn off the Coffee Machine by entering “off” to the prompt.
    # a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
    # the machine. Your code should end execution when this happens.
    if user_request == "off":
        power_status = False
# 3. Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
    elif user_request == "report":
        for item in resources:
            print(f"{item}: {resources[item]}")
        print(f"Money: ${money}")

# 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.

    # resources['milk'] = 20
    # resources['water'] = 20
    # resources['coffee'] = 20
    print(resources)
    if user_request in MENU.keys():
        if check_resource(u=user_request, m=MENU, r=resources) == 1:
            print("Please insert coins.")
            q = int(input("How many quarters?: "))
            d = int(input("How many dimes?: "))
            n = int(input("How many nickles?: "))
            p = int(input("How many pennies?: "))
            total_paid = (q * 0.25) + (d * 0.10) + (n * 0.05) + (p * 0.01)
            cost = MENU[user_request]['cost']
            change = total_paid - cost
            if change >= 0:
                print(f"Here is ${round(change, 2)} dollars in change.")
                print(f"Here is your {user_request}, enjoy")
                k = MENU[user_request]['ingredients']
                for item in resources:
                    if item in k:
                        resources[item] -= k[item]
                        money += cost
                print(f"Remaining resources: {resources}")
            else:
                print("Sorry that's not enough money. Money refunded.")

        else:
            print(f"Sorry there is not enough {check_resource(u=user_request, m=MENU, r=resources)}.")
            power_status = False


# 5. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

# 6. Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected.
# E.g. Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say “Sorry that's not enough money. Money refunded.”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.
# E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
# places.
# 7. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# latte was their choice of drink.
