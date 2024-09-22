from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paying {amount} using Credit Card"
    

class PayPalPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paying {amount} using PayPal"
    

class BitcoinPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paying {amount} using Bitcoin"
    


class ShoppingCart:
    def make_payment(self, amount, payment_method)-> PaymentMethod:
        if payment_method=='Credit Card':
            return CreditCardPayment().pay(amount)
        if payment_method=='PayPal':
            return PayPalPayment().pay(amount)
        else:
            return BitcoinPayment().pay(amount)
        

if __name__=="__main__":
    cart=ShoppingCart()

    type_1 = cart.make_payment( 100, "PayPal")
    print(type_1)

    type_2 = cart.make_payment( 200, "Credit Card")
    print(type_2)

    type_3 = cart.make_payment( 300, "Bitcoin")
    print(type_3)
    
    
    


    

