from LLD.Oops.interface_and_abc.payments_example.payments_interface import PaymentsInterface


class Ach(PaymentsInterface):
    def pay(self,amount):
        print(f"Pay amount {amount} using Ach")


ach = Ach()
ach.pay("200")