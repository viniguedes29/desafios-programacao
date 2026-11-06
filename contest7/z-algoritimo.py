def calcular_z(s):
    n = len(s)
    z = [0] * n
    L = R = 0

    for i in range(1, n):
        if i <= R:
            z[i] = min(z[i - L], R - i + 1)

        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1

        if i + z[i] - 1 > R:
            L = i
            R = i + z[i] - 1

    return z