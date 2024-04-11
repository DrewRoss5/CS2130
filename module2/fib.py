def recursive_fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return recursive_fib(n - 2) + recursive_fib(n - 1)

def fast_fib(n):
    prev = 0
    current = 1
    tmp = 0
    for i in range(n):
        tmp = current + prev
        prev = current
        current = tmp
    return prev

def matrix_fib(n):
    mat = [[1, 1], [1, 0]]
    if n < 2:
        return n
    matrix_pow(mat, n - 1)
    return mat[0][0]

def matrix_pow(A, n):
    if n == 1:
        return
    copy = [[A[0][0], A[0][1]], [A[1][0], A[1][1]]]
    matrix_pow(A, n // 2)
    matrix_multiply(A, A)
    if n % 2 != 0:
        matrix_multiply(A, copy)

def matrix_multiply(A, B):
    w = A[0][0] * B[0][0] + A[0][1] * B[1][0]
    x = A[1][0] * B[0][0] + A[1][1] * B[1][0]
    y = A[0][0] * B[0][1] + A[0][1] * B[1][1]
    z = A[1][0] * B[0][1] + A[1][1] * B[1][1]

    A[0][0] = w
    A[1][0] = x
    A[0][1] = y
    A[1][1] = z
