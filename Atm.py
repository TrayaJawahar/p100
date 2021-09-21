class Atm (object):
    def __init__(self,name,card_no,pin_no,cash_wd,bcash):
        self.name=name
        self.car_no=card_no
        self.pin_no=pin_no
        self.cash_wd=cash_wd
        self.bcash=bcash

    def Cashwithdrawal(self):
        print("Cash Withdraw:",cash_wd)

    def BalanceEnquiry(self):
        print("Balance Cash")

arya=Atm("Arya","123456789012","123","2000","62000")
darsh=Atm("Darsh","098765432109" , "987" , "10000", "90000")

print(arya.Cashwithdrawal())
print(darsh.BalanceEnquiry())