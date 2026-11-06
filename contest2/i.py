
def mat_mul(A, B):
    C = [[0, 0], [0, 0]]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] += A[i][k] * B[k][j] 
            C[i][j] %= (10**9 + 7)

    return C


def mat_pow(M, n):
    R = [[1, 0], [0, 1]]

    while n > 0:
        if n % 2 == 1:
            R = mat_mul(R, M)

        M = mat_mul(M, M)
        n //= 2

    return R


def fibonacci(n):
    M = [
        [1, 1],
        [1, 0]
    ]

    R = mat_pow(M, n)

    return R[0][1]


def main():
    n = int(input())
    print(fibonacci(n))


    

if __name__ == "__main__":
    main()