from tabnanny import check
#This program works best if you are starting the week


class Person:
    def __init__(self,days_per_check, check_amount,bills_total):   
        self.days_per_check = days_per_check
        self.check_amount = check_amount
        self.bills_total = bills_total
        if check_amount > bills_total:
            self.net_check = check_amount - bills_total
    
    dayoftheweek = 0

    def daysleftuntilpaycheck(self):
        return self.days_per_check - self.dayoftheweek 
    
    spendsheet = {}
    for i in range(1, daysleftuntilpaycheck + 1):
        spendsheet[i] = 0
    
    def available_daily(self,daysleftuntilpaycheck):
        return self.total_available/daysleftuntilpaycheck

    def total_spent(self):
        total = 0
        for day, spent in self.spendsheet.items:
            total += spent
        return total

    def total_available(self, net_check):
        available = net_check - self.total_spent()
        return available

    def adding_expenditure(self,expenditure):
        self.spendsheet[self.dayoftheweek] = expenditure

    def whatcanispendtoday(self):
        return self.total_available/self.daysleftuntilpaycheck



Daniel = Person(14,1000,0)
print(Daniel.whatcanispendtoday)
