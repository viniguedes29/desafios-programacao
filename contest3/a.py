
def main():
    entrada = input().split()
    a = int(entrada[0])
    b = int(entrada[1])

    if a==b:
        print(a)
    else:
        print(1)

def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a   

if __name__ == "__main__":
    main()