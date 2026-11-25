from math import pi, asin
def main():
    n, R, r = map(int, input().split())

    if n == 1:
        if  R >= r:
            print("YES")
        else:
            print("NO")
    elif R == r or r > R:
        print("NO")
    elif n == 2:
        if R >=2*r:
            print("YES")
        else:
            print("NO")

    else:
        
        if abs(pi - n*(asin(r/(R-r))) )< 10**-9:
            print("YES")
        elif  pi > n*(asin(r/(R-r))):
            print("YES")
        else:   
            print("NO")

    

if __name__ == "__main__":
    main()