#from collections import deque
from itertools import product

#class Grid:
#    def __init__(self,m,p=None):
#        self.n = len(m)
#        self.matrix = m
#        self.parent = p
#        if self.parent == None:
#            self.h = 0
#        else:
#            self.h = self.parent.h + 1

#    def IsNull(self):
#        for x in self.matrix:
#            for y in x:
#                if y != 0:
#                    return False
#        return True

#    def len(self):
#        if self.parent == None:
#            return 0
#        return self.parent.len() + 1

#    def __repr__(self):
#        return str(self.matrix)

#    def __str__(self):
#        return str(self.matrix)

#def BFS(grid):
#    results = []
#    n = len(grid)
#    for i,j in product(range(0,n),repeat=2):
#        if sum(grid[i]) == 0 and sum(x[j] for x in grid) == 0:
#            continue
#        grid1 = [list(x) for x in grid]
#        for k in range(0,n):
#            grid1[k][j] = grid1[k][j] ^ 1
#            grid1[i][k] = grid1[i][k] ^ 1
#        grid1[i][j] = grid1[i][j] ^ 1
#        results.append(grid1)
#    return results

#def contains(item,items):
#    for it in items:
#        if isEqual(it,item):
#            return True
#    return False

#def isEqual(it,item):
#    n = len(item)
#    for i,j in product(range(n),repeat=2):
#        if it[i][j] != item[i][j]:
#            return False
#    return True

#def equivalentItemIn(item,_global):
#    item1 = [list(x) for x in item]
#    for i in range(4):
#        if contains(item1,_global):
#            return True
#        item1 = rotateLeft(item1)

#    #item2 = FlipHorizontal([list(x) for x in item])
#    #for i in range(4):
#    # if contains(item1,_global):
#    # return True
#    # item2 = rotateLeft(item2)

#    #item3 = FlipVertical([list(x) for x in item])
#    #for i in range(4):
#    # if contains(item1,_global):
#    # return True
#    # item3 = rotateLeft(item3)

#    return False

#def FlipVertical(matrix):
#    n = len(matrix)
#    for x in range(n // 2):
#        matrix[x],matrix[n - 1 - x] = matrix[n - 1 - x],matrix[x]
#    return matrix

#def FlipHorizontal(matrix):
#    n = len(matrix)
#    for x in range(n // 2):
#        for i in range(n):
#            matrix[i][x],matrix[i][n - 1 - x] = matrix[i][n - 1 -
#            x],matrix[i][x]
#    return matrix

#def rotateLeft(matrix):
#    n = len(matrix)
#    m1 = [[0] * n for i in range(n)]
#    for i in range(n):
#        for j in range(n):
#            m1[i][j] = matrix[j][n - 1 - i]
#    return m1

#def add(matrix,_global):
#    item1 = [list(x) for x in matrix]
#    for i in range(4):
#        _global.append(item1)
#        item1 = rotateLeft(item1)

#    item2 = FlipHorizontal([list(x) for x in matrix])
#    for i in range(4):
#        _global.append(item2)
#        item2 = rotateLeft(item2)

#    item3 = FlipVertical([list(x) for x in matrix])
#    for i in range(4):
#        _global.append(item2)
#        item3 = rotateLeft(item3)

#    return _global

#p ={}
#def poww(x):
#    if x not in p:
#        p[x] = 2 ** x
#    return p[x]

#def fingerprint(x):
#    s = ''
#    n=len(x)
#    for i in range(n):
#        q=0
#        for j in range(n):
#            q+=poww(j)*x[i][j]
#        s+=str(q)
#    #for i,j in product(range(len(x)),repeat=2):
#    # s+=(poww(i * len(x) + j)) * x[i][j]
#    return s

#def getAllfingerprints(item):
#    x=[]
#    item1 = [list(x) for x in item]
#    for i in range(4):
#        x.append(fingerprint(item1))
#        item1 = rotateLeft(item1)

#    #item2 = FlipHorizontal([list(x) for x in matrix])
#    #for i in range(4):
#    # x.append(fingerprint(item1))
#    # item2 = rotateLeft(item2)

#    #item3 = FlipVertical([list(x) for x in matrix])
#    #for i in range(4):
#    # x.append(fingerprint(item1))
#    # item3 = rotateLeft(item3)
#    return x

#def answer(matrix):
#    grid = Grid(matrix)
#    #_global = [matrix]
#    _global = [fingerprint(matrix)]
#    todo = deque([grid])

#    while len(todo) != 0:
#        left = todo.popleft()
#        li = BFS(left.matrix)
#        for item in li:
#            if sum(sum(x) for x in item) == 0:
#                return left.h + 1
#        for item in li:
#            if fingerprint(item) not in _global:
#            #if not contains(item,_global):
#            #if not equivalentItemIn(item,_global):
#                todo.append(Grid(item,left))
#                #_global.append(fingerprint(item))
#                _global.extend(getAllfingerprints(item))
#                #_global = add(item,_global)
    
#    return -1
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
#    for i,j in product(range(n),repeat=2):
#        x = (i * n) + j
#        for k,l in product(range(n),repeat=2):
#            if i == k or j == l:
#                y = (k * n) + l
#                result[x][y] = 1
#        result[x][n2] = A[i][j]
#    return result

#def solu(B):
#    n = len(B)
#    A = convert(B) # returns a matrix n squared rows
#    mx = n ** n
#    for s in product([0,1],repeat=len(A)):
#        x = sum(s)
#        if mx <= x:
#            continue
#        fit = True
#        for rel in A:
#            result = 0
#            for i in range(len(s)):
#                result = result ^ (s[i] & rel[i])
#            if result != rel[len(s)]:
#                fit = False
#                break
#        if fit:
#            mx = x
#            if mx == 1:
#                break
#    return mx
def validate(matrix):
    ones = [sum(row) % 2 for row in matrix]
    for i in range(len(matrix)):
        s = 0
        for j in range(len(matrix)):
            if matrix[j][i]:
                s+=1
        ones.append(s % 2)
    if len(set(ones)) == 1:
        return True
    else:
        return False

def answer(matrix):
    n = len(matrix)
    if n % 2 == 0:
        rev = [[0] * n for i in range(n)]
        for i,j in product(range(n),repeat=2):
            if matrix[i][j]:
                for k in range(n):
                    rev[k][j] = rev[k][j] ^ 1
                    rev[i][k] = rev[i][k] ^ 1
                rev[i][j] = rev[i][j] ^ 1
        return sum([sum(row) for row in rev])
    elif validate(matrix):
        condition = True
        for i,j in product(range(n),repeat=2):
            if i == j or i == n - 1 or j == n - 1:
               if matrix[i][j] == 0:
                   condition = False
                   break
            elif matrix[i][j]:
                condition = False
                break
        if condition:
            return n
        return sum([sum(row) for row in matrix])
    else:
        return -1
    #B = convert(matrix)
    #x = gauss(B)
    #y = sum(x) % len(matrix)
    #return y if y > 0 else len(matrix) - 1
    #print()
def main():
    print("[[1,1],[0,0]]")
    print(2 == answer([[1,1],[0,0]]))
    print(-1 == answer([[1,1,1],[1,0,0],[1,0,1]]))
    print("**")
    print(answer([[0,0,1],[0,0,1],[1,1,1]]))
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
    print(answer([[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
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
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]))
if __name__ == "__main__":
    main()