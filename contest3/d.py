
def main():
    n = int(input())
    entradas = []

    for i in range(n):
        entrada = input().split()
        a = int(entrada[0])
        b = int(entrada[1])

        print(a - b)
    

if __name__ == "__main__":
    main()