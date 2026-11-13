# 11.1
import time

n = 50_000_000
target = -1

array_list = list(range(n))
start = time.perf_counter()
found_list = target in array_list
duration_list = time.perf_counter() - start

array_set = set(range(n))
start = time.perf_counter()
found_set = target in array_set
duration_set = time.perf_counter() - start

if duration_set > 0:
  speedup = duration_list / duration_set
else:
  speedup = 0

print(f"Час пошуку у List: {duration_list:.6f} секунд")
print(f"Час пошуку у Set:  {duration_set:.6f} секунд")
print(f"Множина швидша за список у {speedup:,.0f} разів!")

# 11.2
import time

n = 10_000
m = 10_000

list1 = list(range(n))
list2 = list(range(5000, n + 5000))

start = time.perf_counter()

intersection_slow = []
for item in list1:
  if item in list2:
    intersection_slow.append(item)

duration_slow = time.perf_counter() - start

start = time.perf_counter()
intersection_fast = list(set(list1) & set(list2))
duration_fast = time.perf_counter() - start

if duration_fast > 0:
  speedup = duration_slow / duration_fast
else:
  speedup = 0

print(f"Повільний пошук: {duration_slow:.6f} секунд.")
print(f"Швидкий пошук:  {duration_fast:.6f} секунд.")
print(f"Множини швидші у {speedup:,.0f} разів")
