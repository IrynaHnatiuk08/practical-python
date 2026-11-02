# Задача 9.1. Декомпозиція системи аналізу студентських оцінок
grades = [85, 92, 60, 78, 45, 95, 88, 70]


def analyze_student_grades(grades):
    if not grades:
        print("Помилка: список оцінок порожній!")
        return None

    min_grade = grades[0]
    max_grade = grades[0]
    past_exam = 0
    total_sum = 0

    for i in grades:
        total_sum += i

        if i > max_grade:
            max_grade = i
        elif i < min_grade:
            min_grade = i

        if i >= 60:
            past_exam += 1
    average = total_sum / len(grades)

    return max_grade, min_grade, average, past_exam, len(grades)


max_g, min_g, avg, past, total_count = analyze_student_grades(grades)

print(f"Найвищий бал: {max_g}, Найнижчий бал {min_g}, Середній бал групи:{avg}")
print(f"Кількість студентів, які склали іспит: {past} з {total_count} \n")


# Задача 9.2. Валідація та конвертація валют із контрактом (Preconditions)
def convert_currency(amount, rate, source_currency, target_currency):
    if amount <= 0:
        print("Помилка: сума для конвертації має бути більшою за 0")
        return None

    if rate <= 0:
        print("Помилка: курс валюти має бути додатним числом")
        return None

    valid_currencies = ["UAH", "USD", "EUR"]
    if source_currency not in valid_currencies or target_currency not in valid_currencies:
        print("Помилка: одна з валют не підтримується системою")
        return None

    converted_amount = amount * rate
    return converted_amount


result1 = convert_currency(100, 41.5, "USD", "UAH")
print("Результат:", result1)

result2 = convert_currency(-50, 41.5, "USD", "UAH")
print("Результат:", result2)
