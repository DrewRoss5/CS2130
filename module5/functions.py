def geometric_sequence(n, start, ratio):
    prev = start
    seq = [start]
    for i in range(n - 1):
        prev *= ratio
        seq.append(round(prev, 2))
    return seq



def arithmetic_sequence(n, start, difference):
    seq = [start]
    prev = start
    for i in range(n - 1):
        prev += difference
        seq.append(round(prev, 2))
    return seq


def div_mod(dividend, divisor):
    result = 0
    rem = dividend
    if dividend >= 0:
        while (rem >= divisor):
            result += 1
            rem -=  divisor
        return (result, rem)
    else:
        while (rem < 0):
            result -= 1
            rem += divisor
        return (result, rem)

def gcd(x, y):
    if x > y:
        tmp = x
        x = y
        y = tmp
    while y != 0:
        tmp = y
        y = x % y
        x = tmp
    return x


def lcm(x, y):
    denominator = gcd(x, y)
    return (x * y) / denominator
