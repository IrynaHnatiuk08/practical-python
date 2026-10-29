#8.1
#day      1     2    3   4    5    6
prices = [100, 102, 101, 105, 110, 108]
k = 3    # скільки днів у вікні

for i in range(len(prices) - k + 1):
   total = 0

   for j in range(k):
       total = total + prices[i + j]

   average = total / k
   print(f"Вікно з дня {i + 1} - середня ціна: {average:.2f}")
print("\n")

# Задача 8.2. Оптимізація перевірки енергоспоживання за префіксними сумами

# Споживання електроенергії по днях (кВт·год)
energy = [5, 3, 8, 2, 7, 4, 6]
limit = 20

prefix = [0]
for value in energy:
    prefix.append(prefix[-1] + value)

print("Споживання по днях:", energy)
print("Префіксні суми:", prefix)


start = 2
end = 5

total = prefix[end] - prefix[start - 1]
print("Спожито з дня", start, "по день", end, ":", total)


if total > limit:
    print("Перевищення ліміту!")
else:
    print("В нормі")