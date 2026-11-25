from math import pi
def main():
    n = int(input())
    raios = list(map(int, input().split()))

    a = 0
    v = 0 
    raios.sort()
    if n %2 == 0:
        a += raios[0]**2
        for i in range(1, n):
            if i%2 == 1:
                v += raios[i]**2 - raios[i-1]**2
            else:
                a += raios[i]**2 - raios[i-1]**2
    else:
        v += raios[0]**2
        for i in range(1, n):
            if i%2 == 1:
                a += raios[i]**2 - raios[i-1]**2
            else:
                v += raios[i]**2 - raios[i-1]**2

    print(pi*v)

if __name__ == "__main__":
    main()