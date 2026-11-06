def main():
    t =  int(input())
    checks = []
    
    for _ in range(t):
        x = list(map(int, input().split(' ')))
        checks.append(x)

    for c in checks:
        n = c[0]
        v = c[1]

        if n%2 ==0:
            print(n + 2*v)
        else:
            div = min_div(n)
            print(n + div + 2*(v-1))
        # div = min_div(n)

        # if v == 1:
        #     print(n + div)
        #     continue
        
        # for _ in range(v):
        #     q = n // div # v = div*q

        #     # n + f(n) = q*f(n) + f(n) = (q + 1)* f(n)
        #     d = min_div(q + 1)
        #     div = min(div, d)
        #     n = n + div

        # print(n)


        



def min_div(n):
    max = n**0.5
    x = 2

    if n <= 3:
        return n
    while x < max + 1:
        if n % x == 0:
            return x
        x += 1
    return n
if __name__ == "__main__":
    main()
