# Paste your code into this box
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
monthlyInterestRate = annualInterestRate / 12.0

for month in range(1, 13):
    monthlyPayment = balance * monthlyPaymentRate
    remaining = balance - monthlyPayment
    balance = remaining + remaining * monthlyInterestRate      

print("Remaining balance:",round(balance,2))