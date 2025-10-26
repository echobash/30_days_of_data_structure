class Bank:
    def is_valid_transaction(self,account_no):
        return 1 <= account_no <= self.no_of_accounts

    def __init__(self, balance: List[int]):
        self.balance = balance
        self.no_of_accounts = len(self.balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self.is_valid_transaction(account1) or not self.is_valid_transaction(account2):
            return False

        if money >  self.balance[account1 - 1]:
            return False
        
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True


    def deposit(self, account: int, money: int) -> bool:
        if not self.is_valid_transaction(account):
            return False
        
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self.is_valid_transaction(account):
            return False

        if money >  self.balance[account - 1]:
            return False

        self.balance[account - 1] -= money
        return True




# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)