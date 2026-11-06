def main():
    s1 = input()
    s2 = input()

    n = len(s1)
    m = len(s2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if s1[i] == s2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

    resultado = ""
    i = 0
    j = 0

    while i < n and j < m:
        if s1[i] == s2[j]:
            resultado += s1[i]
            i += 1
            j += 1
        elif dp[i + 1][j] >= dp[i][j + 1]:
            i += 1
        else:
            j += 1

    print(resultado)


if __name__ == "__main__":
    main()