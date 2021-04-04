from machine import Machine
from coffee import Coffee


def main():
    not_exit=True
    while not_exit:
        print('Write action (buy, fill, take, remaining, exit): ')
        action=input()
        if action == 'buy':
            print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
            choice=input()

            if choice=='1':
                coffee="espresso"
                machine.buy_coffee(coffee)
            elif choice=='2':
                coffee="latte"
                machine.buy_coffee(coffee)
            elif choice=='3':
                coffee="cappuccino"
                machine.buy_coffee(coffee)
            elif choice=='back':
                pass


        elif action == "fill":
            water=int(input('Write how many ml of water do you want to add: '))
            machine.add_water(water)
            milk=int(input('Write how many ml of milk do you want to add:'))
            machine.add_milk(milk)
            beans=int(input('Write how many grams of coffee beans do you want to add:'))
            machine.add_beans(beans)
            cups=int(input('Write how many disposable cups of coffee do you want to add:'))
            machine.add_cups(cups)
        
    
        elif action == 'take':
            machine.take_money()
            print(f'I gave you ${machine.money}')
        elif action == "remaining":
            machine.print_resources()
        elif action=='exit':
            not_exit=False
    

machine = Machine(400, 540, 120, 550, 9)
while __name__=="__main__":
    main()


