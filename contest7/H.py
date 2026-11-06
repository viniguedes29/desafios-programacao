def main():
    s = input()
    t = len(s)
    
    if t <= 2:
        print("Just a legend")
        return

    lps = compute_lps(s)
    max_val = lps[-1] 


    valores_no_meio = set()
    for j in range(1, t - 1):
        if lps[j] > 0:
            valores_no_meio.add(lps[j])

    while max_val > 0:
        if max_val in valores_no_meio:
            print(s[:max_val]) 
            return
        max_val = lps[max_val - 1]

    print("Just a legend")


    # for i in range(1, t):
    #     #print(prefixo(s, i) + " " + sufixo(s,i) )
    #     if prefixo(s, i) == sufixo(s,i):

    #         candidatos.append(prefixo(s, i))

    # fim = len(candidatos) - 1

    # if len(candidatos) == 0:
    #     print("Just a legend")
    #     return

    # #print(candidatos)
    # ganhador = ""
    # inicio = 0
    
    # #print(candidatos)
    # while inicio <= fim:      
    #     meio = (inicio + fim) // 2
    #     #print(meio)

    #     m = len(kmp(s[1:-1], candidatos[meio]))

    #     if m == 0:
    #         fim = meio - 1
    #     else:
    #         ganhador = candidatos[meio]
    #         inicio = meio + 1

    # if ganhador == "":
    #     print("Just a legend")
    #     return

    # print(ganhador)


def prefixo(s, i):
    return s[0:i]

def sufixo(s, i):
    return s[-i:]

def compute_lps(p):
    m = len(p)
    lps = [0] * m

    length = 0
    i = 1

    while i < m:
        if p[i] == p[length]:
            length += 1
            lps[i] = length
            i += 1

        elif length != 0:
            length = lps[length - 1]

        else:
            lps[i] = 0
            i += 1

    return lps


def kmp(text, pattern):
    if not pattern:
        return list(range(len(text) + 1))

    n = len(text)
    m = len(pattern)

    lps = compute_lps(pattern)
    matches = []

    i = 0 
    j = 0 

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == m:
            matches.append(i - j)
            j = lps[j - 1]

        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches
    

if __name__ == "__main__":
    main()
