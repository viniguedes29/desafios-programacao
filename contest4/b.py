def main():
    entrada = input()
    a, b, c, d = map(int, entrada.split())

    print(a/b * (1/(1 - (1 - a/b)*(1 - c/d))))

if __name__ == "__main__":
    main()
