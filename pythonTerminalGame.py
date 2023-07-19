import pyfiglet

title = pyfiglet.figlet_format(
    "Welcome To Mortgage Calculator", font='xsansi')


class MortgageCalculator:
    name = "Mortgage Calculator"

    def ask_questions(self):
        self.name = input('Whats your name? ')
        self.principle = int(input("How much are you looking to spend? "))
        self.years = int(
            input("How many years will this mortgage be? I.E 15/20/30 years "))
        self.interest_rate = int(
            input("What is your interest rate? ").replace('%', '')) / 100

    def __repr__(self):
        return f"Welcome {self.name} to the Mortgage Calculator!\n" \
               f"You have a mortgage of ${self.to_money(self.principle)}.\n" \
               f"The interest rate is {self.interest_rate * 100}%.\n" \
               f"You will pay ${self.to_money(self.calculate_mortgage())} per month for {self.years} years.\n" \
               f"In total, you will pay ${self.to_money(self.total_payed())} which includes ${self.to_money(self.interest_payed())} in interest."

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
        mortgage = self.calculate_mortgage() * (self.years * 12)
        return mortgage

    def interest_payed(self):
        return self.total_payed() - self.principle

    def start(self):
        # Main program loop
        while True:
            self.ask_questions()
            print(repr(self))
            restart = input("\nWould you like to start again? (yes/no): ")
            if restart.lower() != "yes":
                break


print(title)

mortgage = MortgageCalculator()
mortgage.start()
# Mortage math is principal*Interest(1+interest)^number of payments / (1+r)^n - 1
