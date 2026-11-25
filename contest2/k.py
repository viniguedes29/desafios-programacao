MOD = 10**9 + 7


def main():
    entrada = input().split()
    n = int(entrada[0])

    total = pow(10, n, MOD)
    sem_0 = pow(9, n, MOD)
    sem_9 = pow(9, n, MOD)
    sem_0_e_9 = pow(8, n, MOD)

    resposta = (total - sem_0 - sem_9 + sem_0_e_9) % MOD
    print(resposta)


if __name__ == "__main__":
    main()
