def main():
    entrada = input().split("e")
    a = int(entrada[0].split(".")[0])
    p_dec = entrada[0].split(".")[1]
    t_dec = len(p_dec)
    exp = int(entrada[1])

    if exp == 0 and a != 0:
        print(entrada[0])
        return
    elif a == 0:
        print(0)
        return
    if a == 0:
        a = ""
    else:
        a = str(a)

    if exp >= t_dec:
        print(a + (p_dec + "0" * exp)[:exp])
    else:
        print(a + (p_dec)[:exp] + "." + p_dec[exp:])


if __name__ == "__main__":
    main()
