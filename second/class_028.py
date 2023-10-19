# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10...

 def fibonnacci(n):
    if n <= 1:
        return n
    return fibonnacci(n-1) + fibonnacci(n-2)
print(fibonnacci(10))

def fibonnacci(n):
    a, b = 0, 1
    for item in range(n):
        result = b
        a, b = b, a + b

    return a

print(fibonnacci(10))
assert fibonnacci(10) == 55