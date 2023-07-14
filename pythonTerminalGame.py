import pyfiglet

word = pyfiglet.figlet_format(
    "Welcome To Mortgage Calculator", font='xsansi')


class MortgageCalculator:
    name = "Mortgage Calculator"

    def ask_questions(self):
        self.name = input('Whats your name?')
        self.principle = int(input("How much are you looking to spend?"))
        self.years = int(
            input("How many years will this mortgage be? I.E 15/20/30 years"))
        self.interest_rate = int(input("What is your interest rate?")) / 100

    # def __init__(self, principle, interest_rate, years, name=''):
    #     self.principle = principle
    #     self.interest_rate = interest_rate / 100
    #     self.years = years
    #     self.name = name

    def __repr__(self):
        return f"Welcome {self.name} to Mortgage Calculator with a Mortgage of ${self.to_money(self.total_payed())} and an interest rate of {self.interest_rate * 100}% paying ${self.to_money(self.calculate_mortgage())} per month for {self.years} years resulting in paying ${self.to_money(self.interest_payed())} in interest"

    def to_money(self, input):
        return "{:,.2f}".format(input)

    def calculate_mortgage(self):
        months = self.years * 12
        rate = (self.interest_rate/12)
        power = (rate + 1) ** months
        top = self.principle * rate * power
        bottom = power - 1
        mortgage = top/bottom
        return mortgage

    def total_payed(self):
        mortgage = self.calculate_mortgage() * 360
        return mortgage

    def interest_payed(self):
        return self.total_payed() - self.principle


print(word)

mortgage = MortgageCalculator()
mortgage.ask_questions()
print(mortgage)
# Mortage math is principal*Interest(1+interest)^number of payments / (1+r)^n - 1
