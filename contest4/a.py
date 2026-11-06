def fatorial_mod(n):
    resultado = 1

    for i in range(2, n + 1):
        resultado = resultado * i %  (10**9 + 7)

    return resultado

def mult(a,b):
    return (a % (10**9 + 7) * b % (10**9 + 7)) % (10**9 + 7)
def main():
    entrada = input()
    dicionario = {}

    for caractere in entrada:
        dicionario[caractere] = dicionario.get(caractere, 0) + 1
    fatores = list(dicionario.values())

    numerador = fatorial_mod(len(entrada))
    denominador = 1
    for i in fatores:
        denominador *= fatorial_mod(i)
        denominador = denominador % (10**9 + 7)

    resultado = numerador * pow(denominador, (10**9 + 5), (10**9 + 7))
    resultado = resultado % (10**9 + 7)
        

    print(int(resultado))

if __name__ == "__main__":
    main()