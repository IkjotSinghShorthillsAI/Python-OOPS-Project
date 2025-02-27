import unittest
from bank_accounts import BankAccount, InterestRewardsAcct, SavingsAcct, BalanceException

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(100, "TestAccount")
        self.other_account = BankAccount(50, "OtherAccount")
    
    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)
    
    def test_withdraw_success(self):
        self.account.withdraw(50)
        self.assertEqual(self.account.balance, 50)
    
    def test_withdraw_failure(self):
        with self.assertRaises(BalanceException):
            self.account.viable_transaction(200)
    
    def test_transfer_success(self):
        self.account.transfer(50, self.other_account)
        self.assertEqual(self.account.balance, 50)
        self.assertEqual(self.other_account.balance, 100)
    
    def test_transfer_failure(self):
        with self.assertRaises(BalanceException):
            self.account.viable_transaction(200)

class TestInterestRewardsAcct(unittest.TestCase):
    def setUp(self):
        self.account = InterestRewardsAcct(100, "InterestAccount")
    
    def test_deposit_with_interest(self):
        self.account.deposit(100)
        self.assertEqual(self.account.balance, 205)  # 100 + 100*1.05

class TestSavingsAcct(unittest.TestCase):
    def setUp(self):
        self.account = SavingsAcct(100, "SavingsAccount")
    
    def test_withdraw_with_fee_success(self):
        self.account.withdraw(50)
        self.assertEqual(self.account.balance, 45)  # 100 - 50 - 5
    
    def test_withdraw_with_fee_failure(self):
        with self.assertRaises(BalanceException):
            self.account.viable_transaction(200)

if __name__ == "__main__":
    unittest.main()
