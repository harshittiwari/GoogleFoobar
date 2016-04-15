dictFactorial = {}

def answer(seq):
    if len(seq) == 1:
        return 1
    l1 = []
    l2 = []
    divide(seq,l1,l2)
    cnt = conquer(l1,l2)
    return str(cnt)

def divide(seq,l1,l2):
    root = seq[0]
    for i in range(1,len(seq)):
        if seq[i] < root: l1.append(seq[i])
        else: l2.append(seq[i])
    pass

def conquer(l1,l2):
    i1 = 1
    if len(l1) > 1:i1 = int(answer(l1))

    i2 = 1
    if len(l2) > 1:i2 = int(answer(l2))
    
    ans = factorial(len(l1) + len(l2)) / (factorial(len(l1)) * factorial(len(l2)))
    return int(ans) * i1 * i2

def factorial(num):
    if num < 2: return 1
    if num not in dictFactorial: dictFactorial[num] = factorial(num - 1) * num
    return dictFactorial[num]

def main():
    print(answer([5,9,8,2,1]))

if __name__ == "__main__":
    main()