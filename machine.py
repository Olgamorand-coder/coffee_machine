from coffee import Coffee

class Machine:
    def __init__(self, water, milk, beans, money, cups ):
        self.money=money
        self.water=water
        self.milk=milk
        self.beans=beans
        self.cups=cups
    #@classmethod
    #def print_main_menu(cls):
     #   print(f'The coffee machine has:')
      #  print(f'{cls.water} of water')
       # print(f'{cls.milk} of milk')
       # print(f'{cls.beans} of coffee beans')
       # print(f'{cls.cups} of disposable cups')
       # print(f'{cls.money} of money')
    def print_resources(self):
        print(f'The coffee machine has:')
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.beans} of coffee beans')
        print(f'{self.cups} of disposable cups')
        print(f'{self.money} of money')


    def buy_coffee(self, coffee_type):
        if coffee_type=="cappuccino":
            coffee_type = Coffee(200, 100, 12, 6)

        elif coffee_type=="latte":
            coffee_type = Coffee(350, 75, 20, 7)

        elif coffee_type == "espresso":
            coffee_type = Coffee(250, 0, 16, 4)

        lack_ingred=self.which_lack_ingr(coffee_type.water, coffee_type.milk, coffee_type.beans)
        if lack_ingred==False:
            self.money=self.money+coffee_type.money
            self.water=self.water-coffee_type.water
            self.milk=self.milk-coffee_type.milk
            self.beans=self.beans-coffee_type.beans
            self.cups=self.cups-1
            print('I have enough resources, making you a coffee!')
        else:
            print(f'sorry, not enough {lack_ingred}!')
    
    def add_water(self, added_water):
        self.water+=added_water
    def add_milk(self, added_milk):
        self.milk+=added_milk
    def add_beans(self, added_beans):
        self.beans+=added_beans
    def add_cups(self, added_cups):
        self.cups+=added_cups

    def take_money(self):
        self.money=0

    def which_lack_ingr(self, water, milk, beans):
        if self.water-water>=0:
            if self.milk-milk>=0:
                if self.beans-beans>=0:
                    if self.cups-1>=0:
                        return False
                    else:
                        return 'cups'
                else:
                    return 'beans'
            else:
                return 'milk'
        else:
            return 'water'






#new_machine=Machine(500, 400, 500, 300, 50)


#new_machine.buy_menu()
#new_machine.buy_coffee("espresso")
#print(new_machine.beans(), new_machine.cups(), new_machine.milk(), new_machine.water(), new_machine.money())