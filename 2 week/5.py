from datetime import datetime, timedelta

input_date = input()
date = datetime.strptime(input_date, "%d-%m-%Y")
days_n = date.weekday()  
monday_date = date - timedelta(days=days_n)
print(monday_date.strftime("%d-%m-%Y"))
