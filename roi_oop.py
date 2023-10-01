class ReturnOnInvestment():
    def __init__(self):
        self.income = 0
        self.expenses = 0
        self.monthly_cash_flow = 0
        self.annual_cash_flow = 0
        self.cash_investment = 0
        self.roi = 0

    def monthlyIncome(self):
        print("Let's figure out your total monthly income for your property.")
        rent = input("What is the rental income each month? ")
        if rent == '':
            rent = '0'
        laundry = input("What is the laundry income each month? ")
        if laundry == '':
            laundry = '0'
        misc = input("What other misc income is there from your property each month? ")
        if misc == '':
            misc = '0'
        total_monthly_income = int(rent) + int(laundry) + int(misc)
        self.income = total_monthly_income

    def monthlyExpenses(self):
        total_monthly_expenses = 0
        print("Let's figure out your total monthly expenses for your property.")
        taxes = input("What are the taxes on your property each month? ")
        if taxes == '':
            taxes = '0'
        total_monthly_expenses += int(taxes)
        insurance = input("What is the insurance payment on your property each month? ")
        if insurance == '':
            insurance = '0'
        total_monthly_expenses += int(insurance)
        water = input("What is the water payment on your property each month? ")
        if water == '':
            water = '0'
        total_monthly_expenses += int(water)
        sewer = input("What is the sewer payment on your property each month? ")
        if sewer == '':
            sewer = '0'
        total_monthly_expenses += int(sewer)
        hoa_fee = input("What is the HOA Fee for your property each month? ")
        if hoa_fee == '':
            hoa_fee = '0'
        total_monthly_expenses += int(hoa_fee)
        lawn = input("What is the lawn payment for your property each month? ")
        if lawn == '':
            lawn = '0'
        total_monthly_expenses += int(lawn)
        snow = input("What is the snow payment for your property each month? ")
        if snow == '':
            snow = '0'
        total_monthly_expenses += int(snow)
        vacancy = input("What is the vacancy payment for your property each month? ")
        if vacancy == '':
            vacancy = '0'
        total_monthly_expenses += int(vacancy)
        repairs = input("What is the repairs payment for your property each month? ")
        if repairs == '':
            repairs = '0'
        total_monthly_expenses += int(repairs)
        cap_ex = input("What is the CapEx payment for your property each month? ")
        if cap_ex == '':
            cap_ex = '0'
        total_monthly_expenses += int(cap_ex)
        property_management = input("What is your property management payment for your property each month? ")
        if property_management == '':
            property_management = '0'
        total_monthly_expenses += int(property_management)
        mortgage = input("What is your mortgage payment for your property each month? ")
        if mortgage == '':
            mortgage = '0'
        total_monthly_expenses += int(mortgage)
        misc = input("What other misc expenses are there for your property each month? ")
        if misc == '':
            misc = '0'
        total_monthly_expenses += int(misc)
        self.expenses = total_monthly_expenses

    def monthAnnualCashFlow(self):
        self.monthly_cash_flow = self.income - self.expenses
        self.annual_cash_flow = (self.income - self.expenses) * 12
        
    def cashInvestments(self):
        total_investments = 0
        print("Let's figure out your total investment in your property.")
        down_payment = input("What was the down payment on your property? ")
        if down_payment == '':
            down_payment = '0'
        total_investments += int(down_payment)
        closing_costs = input("What was the closing costs on your property? ")
        if closing_costs == '':
            closing_costs = '0'
        total_investments += int(closing_costs)
        rehab_budget = input("What was the rehab budget on your property? ")
        if rehab_budget == '':
            rehab_budget = '0'
        total_investments += int(rehab_budget)
        misc = input("What other misc investments were there in your property? ")
        if misc == '':
            misc = '0'
        total_investments += int(misc)
        self.cash_investment = total_investments
    
    def cashReturnOnInvestment(self):
        self.roi = (self.annual_cash_flow / self.cash_investment) * 100


my_property = ReturnOnInvestment()

def rentalPropertyCalc():
    print("Welcome to The Rental Property Calculator!\n")

    while True:
        my_property.monthlyIncome()
        print(f"\nYour total monthly income is: ${my_property.income}\n")
        
        my_property.monthlyExpenses()
        print(f"\nYour total monthly expenses are: ${my_property.expenses}\n")

        my_property.monthAnnualCashFlow()
        print(f"\nYour monthly cashflow is: ${my_property.monthly_cash_flow}")
        print(f"Which makes your annual cashflow: ${my_property.annual_cash_flow}\n")
        
        my_property.cashInvestments()
        print(f"Your total cash investments are: ${my_property.cash_investment}\n")

        my_property.cashReturnOnInvestment()
        print(f"Your ROI on your rental property is: {round(my_property.roi, 2)}%")
        break

rentalPropertyCalc()