ticket = 12
tickets_one_show = 174
shows_per_month = 15

month_income = ticket * tickets_one_show * shows_per_month
print(month_income) 

#students discount 65%

month_income_discount = (((tickets_one_show * 0.5)* 0.65) + (tickets_one_show * 0.5))* shows_per_month

print(month_income_discount)

