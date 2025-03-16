from LLD.Oops.interface_and_abc.payments_example.payments_interface import PaymentsInterface


class DebitCard(PaymentsInterface):
    def pay(self,amount):
        print(f"Pay amount {amount} using Debit Card")


debit_card = DebitCard()
debit_card.pay("125")