from LLD.Oops.interface_and_abc.payments_example.payments_interface import PaymentsInterface


class CreditCard(PaymentsInterface):
    def pay(self,amount):
        print(f"Pay amount {amount} using Credit Card")


cc = CreditCard()
cc.pay("120")