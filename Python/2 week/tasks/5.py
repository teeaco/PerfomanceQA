#С клавиатуры вводится дата в формате DD-MM-YYYY. Нужно вывести дату начала недели, к которой относится 
#введенная дата (дата понедельника недели), в таком же формате.
from datetime import datetime, timedelta

input_date = input()
date = datetime.strptime(input_date, "%d-%m-%Y")
days_n = date.weekday()  
monday_date = date - timedelta(days=days_n)
print(monday_date.strftime("%d-%m-%Y"))
