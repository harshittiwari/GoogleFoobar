dictFactorial = {}
def factorial(num):
    if num < 2: return 1
    if num not in dictFactorial: dictFactorial[num] = factorial(num - 1) * num
    return dictFactorial[num]

dictCombination = {}
def combination(n,k):
    if n == k and k == 0:
        return 1
    if n == 0:
        return 0
    if (n,k) not in dictCombination:
        dictCombination[(n,k)] = int(factorial(n) / (factorial(k) * factorial(n - k)))
        dictCombination[(n,n - k)] = dictCombination[(n,k)]
    return dictCombination[(n,k)]
#http://oeis.org/A123527
dictA = {}
def answer(n,k):
    if (n,k) not in dictA:
        t = combination(n,2)
        ret = combination(t,k)
        if k < combination(n - 1,2) + 1:
            for i in range(1,n):
                ni = combination(n - 1, i - 1) 
                x = combination(i,2)
                for j in range(i - 1, min(x,k) + 1): 
                    ret -= ni * combination(combination(n - i,2),k - j) * answer(i, j) 
        dictA[(n,k)] = ret
    return dictA[(n,k)]

#def answer(n,k):
#    t = int((n * (n - 1)) / 2)
#    ret = 0
#    if t >= k:
#        ret = combination(t,k)
#        for i in range(n - 1,1,-1):
#            x = int((i * (i - 1)) / 2)
#            if x >= k:
#                ret -= combination(x,k) * combination(n,i)
#    return ret


#t = total number of possible edges with n nodes
#ret = number of ways of choosing k edges from t nodes
#if k is less than maximum number of nodes possible with (n - 1) nodes + 1
#    for i = 1 to n 
#        ni = number of ways of choosing i - 1 nodes from n-1 nodes
#        x = total number of possible edges with i nodes
#        for j=i-1 to number of edges available i.e. minimum of x and k
#            yy = number of ways of having i nodes connected with j edges
#            ret = ret - yy
def main():
    print("answer(5,5)" + str(answer(5,5)))
    for i in range(1,9):
        for j in range(i - 1,combination(i,2) + 1):
            print(str(answer(i,j)))
if __name__ == "__main__":
    main()