from datetime import date

def gift_count(budget, month, birthdays):
    celebrants = [
        (name, date) for name, date in birthdays.items() if date.month == month
    ]
    
    if not celebrants:
        print("В этом месяце нет именинников.")
        return

    celebrants.sort(key=lambda x: x[1].day)

    gift_amount = budget // len(celebrants)

    celebrants_str = ", ".join(
        f"{name} ({date.strftime('%d.%m.%Y')})" for name, date in celebrants
    )

    print(
        f"Именинники в месяце {month}: {celebrants_str}. "
        f"При бюджете {budget} они получат по {gift_amount} рублей."
    )

workers = {
    "Катя": date(1989, 1, 1),
    "Ваня": date(1971, 1, 6),
    "Рахимджон": date(1965, 5, 6),
    "Орзухон": date(1999, 5, 25),
    "Галя": date(1971, 5, 30),
    "Владимир Владимирович": date(1952, 10, 7),
}

gift_count(20000, 5, workers)
