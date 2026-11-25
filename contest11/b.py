
def main():
    t = int(input())
    for _ in range(t):
        np = int(input())
        ps = list(map(int, input().split()))
        nq = int(input())
        qs = list(map(int, input().split()))

        q_par = 0
        p_par = 0

        for i in ps:
            if i % 2 == 0:
                p_par +=1
        for j in qs:
            if j % 2 == 0:
                q_par +=1

        print(p_par*q_par + (np - p_par)*(nq - q_par) )
        

if __name__ == "__main__":
    main()