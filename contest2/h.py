def main():
    entrada = input()
    l = entrada.lower()
    u = entrada.upper()

    l_c = 0
    u_c = 0

    for i in range(len(entrada)):
        if entrada[i] == l[i]:
            l_c += 1
        if entrada[i] == u[i]:
            u_c += 1

    if u_c > l_c:
        print(u)
    else:
        print(l)
    

if __name__ == "__main__":
    #COmentário pra mandar o código dnv
    main()