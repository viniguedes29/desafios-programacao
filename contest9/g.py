def lcp(a, b):
    i = 0

    while i < len(a) and i < len(b) and a[i] == b[i]:
        i += 1

    return i

def main():
    

if __name__ == "__main__":
    main()