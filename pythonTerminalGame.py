import pyfiglet

word = pyfiglet.figlet_format(
    "Welcome To Mortgage Calculator", font='xsansi')


class MortgageCalculator:
    name = "Mortgage Calculator"

    def __init__(self, principle, interest_rate, years):
        self.principle = principle
        self.interest_rate = interest_rate / 100
        self.years = years

    def __repr__(self):
        return f"Mortgage Calculator with a Mortgage of {self.principle} and an interest rate of {self.interest_rate * 100}% for {self.years} years. "

    def calculate_mortgage(self):
        pass


print(word)

mortgage = MortgageCalculator(principle=300000, years=5, interest_rate=5)
print(mortgage.interest_rate)
# Mortage math is principal*Interest(1+interest)^number of payments / (1+r)^n - 1
