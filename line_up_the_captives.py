dictFactorial = {}

def factorial(num):
    if num < 2: return 1
    if num not in dictFactorial: dictFactorial[num] = factorial(num - 1) * num
    return dictFactorial[num]

def answer(x,y,n):
    #divide
    tallestLPos = x
    tallestRPos = n - y + 1

    if tallestRPos < tallestLPos or tallestLPos < 1 or tallestRPos > n: 
        return "0"
    ans = 0
    #combine
    if x == 1:
        ans = solve(y - 1,n - 1)
    elif y == 1:
        ans = solve(x - 1,n - 1)
    else:
        for i in range(tallestLPos,tallestRPos + 1):
            temp = int(factorial(n - 1) / (factorial(i - 1) * factorial(n - i)))
            ans += solve(x - 1,i - 1) * solve(y - 1,n - i) * temp
    return str(ans)

vcDict = {}
def solve(visible, count):
    if (visible, count) in vcDict:
        return vcDict[(visible, count)]

    ret = 0
    if visible == 1:
        ret = factorial(count - 1)
    else:
        for x in range(1,count - visible + 2):
            ret += int(answer(visible,x,count))
        #ret = int(ret * factorial(tot) / (factorial(tot - count)))
        if ret == 0: 
            ret = 1
        vcDict[(visible, count)] = ret
    return ret

def main():
    #print(answer(6, 0, 6))
    print(answer(2, 2, 3))
    print(answer(1, 2, 6))
    #print(answer(3, 2, 6))
    print(answer(5,10,20))
    print(answer(5,10,30))

if __name__ == "__main__":
    main()