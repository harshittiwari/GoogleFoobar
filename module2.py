from itertools import product


MEMO = {}


def bits(iterable):
    bit = 1
    res = 0
    for elem in iterable:
        if elem:
            res |= bit
        bit <<= 1
    return res


def mask(current, n):
    if (current, n) in MEMO:
        return MEMO[(current, n)]

    result = 0
    if current < n:
        for j in range(n):
            result += (2 ** ((current - 1)*n + j) + 2 ** (current*n + j))
    else:
        for i in range(n):
            result += (2 ** (i*n + current - n) + 2 ** (i*n + current - n + 1))

    MEMO[(current, n)] = result

    return result


# See: http://math.stackexchange.com/a/441697/4471
def check(matrix, n):
    parities = [sum(row) % 2 for row in matrix]
    for i in range(n):
        parities.append(sum([row[i] for row in matrix]) % 2)

    return len(set(parities)) == 1


def minimize(matrix, current, n):
    if current == 0:
        # See: http://stackoverflow.com/a/9831671/374865
        return bin(matrix).count("1")
    else:
        return min(minimize(matrix ^ mask(current, n), current - 1, n),
                   minimize(matrix, current - 1, n))


def solve(matrix, n):
    result = [0 for i in range(n) for j in range(n)]

    for i, j in product(range(n), repeat=2):
        if matrix[i][j]:
            for k in range(n):
                result[i*n + k] ^= 1
                result[k*n + j] ^= 1
            result[i*n + j] ^= 1

    if n % 2 == 0:
        return sum(result)
    else:
        return minimize(bits(result), 2*n - 2, n)


def answer(matrix):
    n = len(matrix)

    if n % 2 == 0:
        return solve(matrix, n)
    else:
        if check(matrix, n):
            return solve(matrix, n)
        else:
            return -1


#def pprint(A):
#    n = len(A)
#    for i in range(0, n):
#        line = ""
#        for j in range(0, n + 1):
#            line += str(A[i][j]) + "\t"
#            if j == n - 1:
#                line += "| "
#        print(line)
#    print("")


#def gauss(A):
#    n = len(A)

#    for i in range(0, n):
#        # Search for maximum in this column
#        maxEl = abs(A[i][i])
#        maxRow = i
#        for k in range(i + 1, n):
#            if abs(A[k][i]) > maxEl:
#                maxEl = abs(A[k][i])
#                maxRow = k

#        # Swap maximum row with current row (column by column)
#        for k in range(i, n + 1):
#            tmp = A[maxRow][k]
#            A[maxRow][k] = A[i][k]
#            A[i][k] = tmp

#        # Make all rows below this one 0 in current column
#        for k in range(i + 1, n):
#            c = 0 if A[i][i] == 0 else -A[k][i] / A[i][i]
#            for j in range(i, n + 1):
#                if i == j:
#                    A[k][j] = 0
#                else:
#                    A[k][j] = (A[k][j] + (c * A[i][j])) % 2

#    # Solve equation Ax=b for an upper triangular matrix A
#    x = [0 for i in range(n)]
#    for i in range(n - 1, -1, -1):
#        x[i] = 0 if A[i][i] == 0 else (A[i][n] / A[i][i]) % 2
#        for k in range(i - 1, -1, -1):
#            A[k][n] -= A[k][i] * x[i]
#    return x

#def convert(A):
#    n = len(A)
#    n2 = n * n
#    result = [[0] * ((n2) + 1) for i in range(n2)]
#    for i in range(n):
#        for j in range(n):
#            x = (i * n) + j
#            for k in range(n):
#                for l in range(n):
#                    if i == k or j == l:
#                        y = (k * n) + l 
#                        result[x][y] = 1
#            result[x][n2] = A[i][j]
#    return result

#def eqconvert(A):
#    n = len(A)
#    n2 = n * n
#    result = [[0] * ((n2) + 1) for i in range(n2)]
#    for i in range(n):
#        for j in range(n):
#            x = (i * n) + j
#            for k in range(n):
#                for l in range(n):
#                    if i == k or j == l:
#                        y = (k * n) + l 
#                        result[x][y] = str("x(" + str(k) + "," + str(l) + ")")
#            result[x][n2] = A[i][j]
#    return result

#def possibleSolutions(n):
#    import itertools
#    return list()

def solu(B):
    import itertools
    n = len(B)
    A = convert(B) # returns a matrix n squared rows 
    mx = n ** n
    for s in itertools.product([0,1],repeat=len(A)):
        x = sum(s)
        if mx <= x:
            continue
        fit = True
        for rel in A:
            result = 0
            for i in range(len(s)):
                result = result ^ (s[i] & rel[i])
            if result != rel[len(s)]:
                fit = False
                break
        if fit:
            mx = x
            if mx == 1:
                break
    return mx

if __name__ == "__main__":
    #from fractions import Fraction
    #n = input()

    #A = [[0 for j in range(n+1)] for i in range(n)]

    ## Read input data
    #for i in range(0, n):
    #    line = map(Fraction, raw_input().split(" "))
    #    for j, el in enumerate(line):
    #        A[i][j] = el
    #raw_input()

    #line = raw_input().split(" ")
    #lastLine = map(Fraction, line)
    #for i in range(0, n):
    #    A[i][n] = lastLine[i]

    A = [[1,1,1,0,1],[1,1,0,1,1],[1,0,1,1,0],[0,1,1,1,0]]
    n = 4
    
    #print(sol)
    # Print input
    #pprint(A)

    

    # Calculate solution
    #x = gauss(A)

    ## Print result
    #line = "Result:\t"
    #for i in range(0, n):
    #    line += str(x[i]) + "\t"
    #print(line)

    A = [[1,1],[0,0]]
    print(answer(A))
    #print(solu(A))
    #B = convert(A)
    #pprint(B)
    #x = gauss(B)
    #print(x)
    #print(sum(x))

    A = [[0,0,1],[0,0,1],[1,1,1]]
    print(answer(A))
    #print(solu(A))
    #B = convert(A)
    #pprint(B)
    #x = gauss(B)
    #C = eqconvert(A)
    #pprint(C)
    #print(x)
    #print(sum(x))

    A = [[0,0,0,0,1],[0,0,0,0,1],[0,0,0,0,1],[0,0,0,0,1],[1,1,1,1,1]]
    print(answer(A))
    #print(solu(A))
    #B = convert(A)
    #pprint(B)
    #x = gauss(B)
    #print(x)
    #print(sum(x) % (len(A) - 1))

    A = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    print(answer(A))
    #print(solu(A))
    #B = convert(A)
    #x = gauss(B)
    #print(sum(x) % (len(A) - 1))

    A = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]]
    print(answer(A))
    #print(solu(A))
    #B = convert(A)
    #x = gauss(B)
    #print(sum(x) % (len(A) - 1))
