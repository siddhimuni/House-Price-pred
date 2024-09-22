from abc import ABC, abstractmethod


class coffee(ABC):
    @abstractmethod
    def prepare(self):
        pass


class Espresso(coffee):
    def prepare(self):
        return "Preparing a strong Espresso"
    

class Latte(coffee):
    def prepare(self):
        return "Preparing a smooth creamy latte"
    

class Cappucino(coffee):
    def prepare(self):
        return "Preparing a frothy cappucino"
    



class CoffeeMachine:
    def make_coffee(self, coffee_type) ->coffee:
        if coffee_type=="Espresso":
            return Espresso().prepare()

        if coffee_type=="Latte":
            return Latte().prepare()

        if coffee_type=="Cappucino":
            return Cappucino().prepare()
        
        else:
            return "Unknown coffee type"
        

if __name__=="__main__":
    coffee=CoffeeMachine()

    type_1 = coffee.make_coffee("Espresso")
    print(type_1)

    type_2 = coffee.make_coffee("Latte")
    print(type_2)

    type_3 = coffee.make_coffee("Cappucino")
    print(type_3) 
