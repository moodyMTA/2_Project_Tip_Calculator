print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))

tip = int(input(
    "What percentage tip would you like to give? 10, 12, or 15? "))

people = int(input("How many people to split the bill? "))

each_pay = (tip / 100 * bill + bill) / people

round_each_pay = "{:.2f}".format(each_pay)    # <--- Форматирование в строку.

print(f"Each person should pay: ${round_each_pay}")
