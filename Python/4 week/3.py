import json

def mean_age(json_string: str) -> str:
    data = json.loads(json_string)
    ages = [person["age"] for person in data]
    mean_age_value = sum(ages) / len(ages)
    result = {"mean_age": mean_age_value}
    return json.dumps(result)

