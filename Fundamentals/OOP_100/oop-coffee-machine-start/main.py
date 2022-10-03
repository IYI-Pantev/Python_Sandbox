#Program Requirement:
#1.Print report.
#2.Check resources sufficient?
#3.Process coins.
#4.Check transaction successful?
#5.Make Coffee.

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
is_on = True
# four classes

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

#2.check resources

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        # 1. report
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        #2. check resources
        if coffee_maker.is_resource_sufficient(drink):
            #3.process coins and 4.check transaction
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

