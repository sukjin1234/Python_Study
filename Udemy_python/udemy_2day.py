print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
tips = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people_number = int(input("How many people to split the bill? "))
real_total_bill = (total_bill*((100+tips)/100)/people_number)
final_total = round(real_total_bill,2) #소수점 2번째 반올림해서 표현
final_total = "{:.2f}". format(real_total_bill) #소수점 2번째자리까지 표현 (ex 33.6 (x) 33.60 (o)
print(f"Each person should pay: ${final_total}")