

def main():
    n, k = map(int, input().split())
    s = input()

    sufixo = s
    prefixo = s
    if n == 1:
        print(s*k)
        return

    for i in range(n - 1, 0, -1):
        p = s[:i]
        f = s[i:]
        #print(p + " + " + f)
        #print(f + " + " + p)
        #print("______________")
        if (s + f)[-n:] == s:
            prefixo = p
            sufixo = f
            #print(s+f + "<-")
            break
            
    print(s + sufixo*(k-1))


if __name__ == "__main__":
    main()