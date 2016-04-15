def answer(food,grid):
    matrix = [[set() for y in x] for x in grid]
    matrix[0][0].add(food)
    lg = len(grid)
    for x in range(lg):
        for y in range(lg):
            if x == 0 and y == 0: continue
            if x == 0:
                matrix[x][y].add(next(iter(matrix[x][y - 1])) - grid[x][y])
            elif y == 0:
                matrix[x][y].add(next(iter(matrix[x - 1][y])) - grid[x][y])
            else:
                for el in matrix[x - 1][y]:
                    matrix[x][y].add(el - grid[x][y])
                for el in matrix[x][y - 1]:
                    matrix[x][y].add(el - grid[x][y])
    x = -1
    for el in matrix[lg - 1][lg - 1]:
        if el >= 0 and (el < x or x<0):x = el
    return x

def main():
    print(answer(7,[[0,2,5],[1,1,3],[2,1,1]]))

    print(answer(12,[[0,2,5],[1,1,3],[2,1,1]]))

    print(answer(3,[[0,2,5],[1,1,3],[2,1,1]]))

if __name__ == '__main__':
    main()