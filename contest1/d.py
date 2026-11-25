def main():
    n = int(input())
    d = list(map(int, input().split()))

    prefix_s = [0]*n
    p_ac = 0
    sufix_s = [0]*n
    total = sum(d)

    if n == 1:
        print(0)
        return


    for i in range(n):
        p_ac += d[i]
        prefix_s[i] = p_ac

    p_ac = 0
    for i in range(n):
        sufix_s[i] =  total - prefix_s[i] + d[i]
        p_ac += d[i]

    # print(f"sufixo {sufix_s}")
    # print(f"prefixo {prefix_s}")

    p = 0
    s = n - 1
    p_r = -1
    s_r = -1

    while p < s:
        if sufix_s[s] == prefix_s[p]:
            p_r = p
            s_r = s
            p += 1
            s -= 1
        elif sufix_s[s] > prefix_s[p]:
            p+=1
        else:
            s -=1

    if p_r == -1:
        print(0)
    else:
        print(prefix_s[p_r])
            
        



if __name__ == "__main__":
    main()