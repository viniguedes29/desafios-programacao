def main():
    entrada = input()
    a, b = map(int, entrada.split())

    m = max(a,b)

    if m == 1:
        print("1/1")
    elif m ==2:
        print("5/6")
    elif m ==6:
        print("1/6")
    elif m ==3:
        print("2/3")
    elif m ==4:
        print("1/2")
    elif m ==5:
        print("1/3")
        

if __name__ == "__main__":
    main()
