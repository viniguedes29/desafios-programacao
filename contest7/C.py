def main():
    q = int(input())
    casos = []

    for _ in range(q):
        x = input()
        y = input()
        casos.append([x, y])

    #print(casos)
    for s in casos:
        s1 = s[0]
        s2 = s[1]

        ss1, q1 = fatora_string(s1)
        ss2, q2 = fatora_string(s2)

        #print(ss1 + " " + str(q1) + ", " + ss2 +" " +  str(q2))
        if ss1 == ss2:
            m = mdc(q1,q2)
            if m == 1:
                print(ss1*q1*q2)
            else:
                print(ss1*(m*(q1 // m) * (q2 // m)))
            continue

        print(-1)
        
    
    
        

def fatora_string(s):

    t = len(s)
    q = 1 # s = q*sub
    sub = ""

    for i in range(0, t):
        if t % (i+1) == 0:
            sub = s[:i+1]
            q = i+1
            #print(sub + " " + str(q))


            if s == sub * (t // q):
                #print(f"{sub, q}")
                return sub, t // q
    #print(f"{s, t}")
    return s, t

def mdc(a, b):
  while b:
    a, b = b, a % b
  return a



        
if __name__ == "__main__":
    main()
