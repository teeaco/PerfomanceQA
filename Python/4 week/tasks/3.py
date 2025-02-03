import json
#Задачи, аналогичные этой, часто встречаются в реальной веб-разработке. 
#Будем получать и отдавать JSONы. К вам поступают данные в виде json-строки, 
# в которых содержится список людей. Для каждого человека описаны различные его параметры, но вам 
# нужно посчитать просто средний возраст всех людей из списка. Напишите функцию mean_age(json_string), 
# которая принимает json строку, считает средний возраст людей из входных 
#данных и возвращает новую json-строку в том формате, который указан ниже.
def mean_age(json_string: str) -> str:
    data = json.loads(json_string)
    ages = [person["age"] for person in data]
    mean_age_value = sum(ages) / len(ages)
    result = {"mean_age": mean_age_value}
    return json.dumps(result)

