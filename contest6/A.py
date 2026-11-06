def main():
    t = int(input())
    checks = []

    for _ in range(t):
        y = input()
        x = list(map(int, input().split(' ')))
        checks.append(x)

    for l in checks:


        if len(l) == 1:
            print("YES")
            continue
        
        num = l[0]

        controle = False
        if num % 10 == 5:
            for n in l:
                if n != num:
                    if n == num + 5:
                        continue
                    
                    controle =True
                    break

            if controle:
                print("NO")
            else:
                print("YES")

            continue

        if num % 10 == 0:
            for n in l:
                if n != num:
                    if n == num - 5:
                        continue
                    
                    controle = True
                    break

            if controle:
                print("NO")
            else:
                print("YES")

            continue

            


        g = grupo(l[0])

        controle = False
        for n in l:
            if grupo(n) != g:
                controle = True
                break
        if controle:
            print("NO")
            continue

        
        print("YES")

def grupo(x):
    x = x + x%10
    if x % 40 in [2, 4, 8, 16, 22, 24, 28, 36]:
        return 1
    elif x % 5 == 0:
        return 2
    else:
        return 3

        


if __name__ == "__main__":
    main()
