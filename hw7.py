n = 30
sum_primes = 0

for i in range(2, n + 1):
    is_prime = True

    for e in range(2, i):
        if i % e == 0:
            is_prime = False
            break

    if is_prime:
        sum_primes += i

print(f"Сума всіх простих чисел у діапазоні від 2 до {n} дорівнює: {sum_primes}")