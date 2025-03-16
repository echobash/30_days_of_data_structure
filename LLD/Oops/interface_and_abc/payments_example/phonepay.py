from LLD.Oops.interface_and_abc.payments_example.payments_interface import PaymentsInterface


class PhonePay(PaymentsInterface):
    def pay(self,amount):
        print(f"Pay amount {amount} using PhonePay")


phone_pay = PhonePay()
phone_pay.pay("150")