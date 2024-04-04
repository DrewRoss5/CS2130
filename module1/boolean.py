def multiply(x, y):
    return x * y


def add(x, y):
    result = x + y
    if result > 1:
        result = 1
    return result


def complement(x):
    return [1, 0][x]


def expression1(x, y, z):
    return add(multiply(y, z), multiply(y, add(x , z)))


def expression2(x, y, z):
    return add(multiply(x, complement(y)), (add(x, complement(z))))


def expression3(x, y, z):
    neg_x = complement(x)
    return add(multiply(add(neg_x, y), complement(add(y, z))), multiply(multiply(neg_x, y), z))