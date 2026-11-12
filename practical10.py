#10.1
a = int(input())
n = int(input())
def power(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        half = power(a, n // 2)
        return half * half
    return a * power(a, n - 1)


print(power(a, n))



#10.2
def generate(s, left, right):
    if left == 0 and right == 0:
        print(s)
        return

    if left > 0:
        generate(s + "(", left - 1, right)

    if right > left:
        generate(s + ")", left, right - 1)

n = int(input())
generate("", n, n)
