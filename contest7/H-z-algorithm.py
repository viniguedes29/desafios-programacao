def main():
    s = input()

    z = calcula_z(s)
    n = len(z)

    M = 0
    for i in range(n):
        m = min(z[i], n - i - 1)
        M = max(m, M)

    if M == 0:
        print("Just a legend")
        return
    
    for k in range(M, 0, -1):
        if z[n - k] == k:
            print(s[:k])
            return

    print("Just a legend")




def calcula_z(s):
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


if __name__ == "__main__":
    main()
