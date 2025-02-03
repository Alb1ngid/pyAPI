import requests


def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rates = data.get("rates", {})
        return rates.get(target_currency, None)
    else:
        print("Ошибка запроса API")
        return None


def convert_currency(amount, base_currency, target_currency):
    rate = get_exchange_rate(base_currency, target_currency)
    if rate:
        return amount * rate
    else:
        print("Ошибка: не удалось получить курс обмена.")
        return None


def main():
    popular_currencies = ["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", "SEK", "NZD"]
    print("Популярные валюты:", ", ".join(popular_currencies))

    while True:
        base_currency = input("Введите базовую валюту (например, USD): ").upper()
        target_currency = input("Введите целевую валюту (например, EUR): ").upper()

        if base_currency not in popular_currencies and target_currency not in popular_currencies:
            print("Предупреждение: Вы выбрали менее популярные валюты. Убедитесь, что они доступны.")

        try:
            amount = float(input("Введите сумму: "))
            if amount <= 0:
                print("Ошибка: Сумма должна быть положительным числом.")
                continue
        except ValueError:
            print("Ошибка: Введите корректное число.")
            continue

        result = convert_currency(amount, base_currency, target_currency)
        if result:
            print(f"{amount} {base_currency} = {result:.2f} {target_currency}")

        exit_choice = input("Хотите выполнить еще одну конвертацию? (да/нет): ").strip().lower()
        if exit_choice not in ["да", "yes", "y"]:
            print("Выход из программы.")
            break



if __name__ == "__main__":
    main()
