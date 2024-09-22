from abc import ABC, abstractmethod


class DiningExperience(ABC):

    def serve_dinner(self):
        self.serve_appetizer()
        self.serve_main_course()
        self.serve_dessert()
        self.serve_beverage()


    @abstractmethod
    def serve_appetizer(self):
        pass

    @abstractmethod
    def serve_main_course(self):
        pass

    @abstractmethod
    def serve_dessert(self):
        pass


    @abstractmethod
    def serve_beverage(self):
        pass



class ItalianDinner(DiningExperience):


    def serve_appetizer(self):
        print("Serving bruschetta as appetizer")

    def serve_main_course(self):
        print("Serving pasta as main course")

    
    def serve_dessert(self):
        print("Serving tiramisu as dessert")

    def serve_beverage(self):
        print("Serving wine as beverage")


class ChinesenDinner(DiningExperience):


    def serve_appetizer(self):
        print("Serving spring rolls as appetizer")

    def serve_main_course(self):
        print("Serving noodles as main course")

    
    def serve_dessert(self):
        print("Serving cookies as dessert")

    
    def serve_beverage(self):
        print("Serving tea as beverage")





if __name__=="__main__":
    
    print("Servng Italian dinner")
    italian = ItalianDinner()
    italian.serve_dinner()

    print("\n Chinese Dinner")
    chinese = ChinesenDinner()
    chinese.serve_dinner()


    