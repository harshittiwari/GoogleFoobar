## t steps
## n spots
#def answer(t,n):
#    return ans(t,n) % 123454321

#def answer(t,n):
#    cur = [0 for x in range(n)]
#    cur[n - 1] = 1

#    end = [0 for x in range(n)]

#    for i in range(t):
#        end,cur = cur,end

#        for j in range(n):

#            cur[j] = end[j]

#            if j + 1 == n:
#                continue

#            if j != 0:
#                cur[j]+=end[j - 1]

#            cur[j]+=end[j + 1]

#    return cur[0] % 123454321
#    pass

def answer(t,n):
    previous = [0 for x in range(n)]
    previous[0] = 1
    if len(previous) > 1:
        previous[1] = 1
    tab = []
    tab.append(previous)
    
    for i in range(1,t):
        present = [0 for x in range(n)]
        for j in range(n):
            present[j] = previous[j]
            
            if j != 0:
                present[j]+=previous[j - 1]
            if j + 1 >= n - 1:
                continue
            present[j]+=previous[j + 1]
            if present[j] == 0:
                break
        previous = present
        tab.append(previous)
    print('\n'.join(['{:6}'.format(row+1) + ''.join(['{:6}'.format(item) for item in tab[row]]) 
      for row in range(len(tab))]))
    return previous[len(previous) - 1] % 123454321

def main():
    #print(1 == answer(1,2))
    #print(3 == answer(3,2))
    #print(1 == answer(9,10))
    #print(10 == answer(10,10))
    print(63 == answer(11,10))
    #print(20636 == answer(15,10))
    #print(28107209 == answer(21,10))
    #print(87854134 == answer(22,10))
    #print(60996905 == answer(500,100))
    #print(1 == answer(10,1))
    #print(0 == answer(0,10))
    #print(0 == answer(10,100))

if __name__ == "__main__":
    main()