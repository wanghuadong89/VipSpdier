'''
def qingWa(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return qingWa(n-1) + qingWa(n-2)

def qingWa(n):
    if n == 1 or n == 2:
        return n
    a = 1
    b = 2
    c = 3
    for i in range(3, n + 1):
        c = a + b
        a = b
        b = c
    return c
'''
def qingWa(n):
    def jieCheng(n):
        result = 1
        for i in range(1,n+1):
            result *= i
        return result
    num = 0
    for x in range(int(n/2+1)):
        num += int(jieCheng(x+n-2*x)/jieCheng(n-2*x)/jieCheng(x))
    return num
print(qingWa(100))




