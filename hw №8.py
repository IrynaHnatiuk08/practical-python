
def find_max_subarray(arr):
  potochna_sum = arr[0]
  max_sum = arr[0]

  start = 0
  end = 0
  temp_start = 0

  for i in range(1, len(arr)):

    if arr[i] > potochna_sum + arr[i]:
      potochna_sum = arr[i]
      temp_start = i

    else:
      potochna_sum = potochna_sum + arr[i]


    if potochna_sum > max_sum:
      max_sum = potochna_sum
      start = temp_start
      end = i 

  subarra = arr[start : end + 1]

  return subarra, max_sum


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
subarray, total_sum = find_max_subarray(arr)

print(f" Максимальна сума підмасиву {subarray}: {total_sum}")

