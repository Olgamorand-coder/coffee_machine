class Coffee:
    def __init__(self, water, milk, beans, money):
        self.water=water
        self.beans=beans
        self.milk=milk
        self.money=money
'''     
has_water=int(input('Write how many ml of water the coffee machine has:'))
has_milk=int(input('Write how many ml of milk the coffee machine has:'))
has_beans=int(input('Write how many grams of coffee beans the coffee machine has:'))
#print('Starting to make a coffee\nGrinding coffee beans\nBoiling water\nMixing boiled water with crushed coffee beans\nPouring coffee into the cup\nPouring some milk into the cup\nCoffee is ready!\n')
number_cups=int(input('Write how many cups of coffee you will need: '))
cups_for_engred_dict={'water':'', 'milk':'', 'beans':''}
cups_for_engred_dict['water']=has_water//200
cups_for_engred_dict['milk']=has_milk//50
cups_for_engred_dict['beans']=has_beans//15
key_min=min(cups_for_engred_dict.keys(), key=(lambda k: cups_for_engred_dict[k]))
key_max=max(cups_for_engred_dict.keys(), key=(lambda k: cups_for_engred_dict[k]))
min_cups_possible=cups_for_engred_dict[key_min]

if number_cups==min_cups_possible:
    print('Yes, I can make that amount of coffee')
elif number_cups<min_cups_possible:
    print(f'Yes, I can make that amount of coffee (and even {min_cups_possible-number_cups} more than that)')
else:
    print(f'No, I can make only {min_cups_possible} cups of coffee')'''