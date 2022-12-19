from datetime import date 

today = date.today()
recycle_date = date(2022,12,13) # Just a known recycle day
delta = today - recycle_date
current_delta = delta.days % 14
if current_delta < 8:
	response = "No, it is not a recycle week."
else:
	response = "Yes, it is a recycle week."
print(response)